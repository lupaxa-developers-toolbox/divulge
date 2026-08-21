"""Global configure on the shared engine."""

from __future__ import annotations

import pytest

from lupaxa.divulge.engine import default
from tests.painted import painted


def test_configure_disables_colours_and_prefixes(capsys: pytest.CaptureFixture[str]) -> None:
    default.configure(use_colours=False, use_prefixes=False)
    default.info("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"


def test_configure_enables_bold(capsys: pytest.CaptureFixture[str]) -> None:
    default.configure(use_bold=True)
    default.info("hello")
    captured = capsys.readouterr()
    assert captured.out == f"{painted('[ Info ] hello', 'light_cyan', bold=True)}\n"


def test_configure_ignores_unknown_keys(capsys: pytest.CaptureFixture[str]) -> None:
    default.configure(not_a_key=True, color="light_red", use_colors=False)
    default.info("hello")
    captured = capsys.readouterr()
    assert captured.out == f"{painted('[ Info ] hello', 'light_cyan')}\n"
