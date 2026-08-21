"""Chainable Divulge wrapper and sugar helper."""

from __future__ import annotations

import pytest

from lupaxa.divulge import Divulge, divulge
from lupaxa.divulge.engine import Engine
from tests.painted import painted


def test_wrapper_and_sugar_are_same_type() -> None:
    wrapper = divulge("hello")
    assert isinstance(wrapper, Divulge)
    assert wrapper.value == "hello"


def test_chaining_returns_self_and_prints_each_level(
    capsys: pytest.CaptureFixture[str],
) -> None:
    wrapper = Divulge("msg")
    assert wrapper.info().success().system() is wrapper
    captured = capsys.readouterr()
    assert captured.out == (
        f"{painted('[ Info ] msg', 'light_cyan')}\n"
        f"{painted('[ Success ] msg', 'light_green')}\n"
        f"{painted('[ System ] msg', 'dark_grey')}\n"
    )


def test_wrapper_and_engine_aliases() -> None:
    assert Divulge.warn is Divulge.warning
    assert Divulge.ok is Divulge.success
    assert Engine.warn is Engine.warning
    assert Engine.ok is Engine.success


def test_wrapper_error_and_warning_write_stderr(
    capsys: pytest.CaptureFixture[str],
) -> None:
    Divulge("x").error()
    captured = capsys.readouterr()
    assert captured.err == f"{painted('[ Error ] x', 'light_red')}\n"
    assert captured.out == ""

    Divulge("x").warning()
    captured = capsys.readouterr()
    assert captured.err == f"{painted('[ Warning ] x', 'light_yellow')}\n"
    assert captured.out == ""
