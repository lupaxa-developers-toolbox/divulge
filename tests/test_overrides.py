"""Per-call prefix and colour overrides."""

from __future__ import annotations

import pytest

from lupaxa.divulge.engine import default
from tests.painted import painted


def test_prefix_and_colour_override(capsys: pytest.CaptureFixture[str]) -> None:
    default.info("hello", prefix="[ TIME ]", colour="light_green")
    captured = capsys.readouterr()
    assert captured.out == f"{painted('[ TIME ] hello', 'light_green')}\n"


def test_us_spelling_color_override(capsys: pytest.CaptureFixture[str]) -> None:
    default.system("hello", color="light_red")
    captured = capsys.readouterr()
    assert captured.out == f"{painted('[ System ] hello', 'light_red')}\n"


def test_per_call_use_bold(capsys: pytest.CaptureFixture[str]) -> None:
    default.info("hello", use_bold=True)
    captured = capsys.readouterr()
    assert captured.out == f"{painted('[ Info ] hello', 'light_cyan', bold=True)}\n"


def test_unknown_colour_prints_plain_text(capsys: pytest.CaptureFixture[str]) -> None:
    default.info("hello", colour="not-a-colour")
    captured = capsys.readouterr()
    assert captured.out == "[ Info ] hello\n"
