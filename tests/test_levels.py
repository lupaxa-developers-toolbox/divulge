"""Default prefixes, colours, and streams for each level."""

from __future__ import annotations

import pytest

from lupaxa.divulge.engine import default
from tests.painted import painted


def test_info_writes_cyan_prefix_to_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    default.info("hello")
    captured = capsys.readouterr()
    assert captured.out == f"{painted('[ Info ] hello', 'light_cyan')}\n"
    assert captured.err == ""


def test_success_writes_green_prefix_to_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    default.success("hello")
    captured = capsys.readouterr()
    assert captured.out == f"{painted('[ Success ] hello', 'light_green')}\n"
    assert captured.err == ""


def test_warning_writes_yellow_prefix_to_stderr(capsys: pytest.CaptureFixture[str]) -> None:
    default.warning("hello")
    captured = capsys.readouterr()
    assert captured.err == f"{painted('[ Warning ] hello', 'light_yellow')}\n"
    assert captured.out == ""


def test_error_writes_red_prefix_to_stderr(capsys: pytest.CaptureFixture[str]) -> None:
    default.error("hello")
    captured = capsys.readouterr()
    assert captured.err == f"{painted('[ Error ] hello', 'light_red')}\n"
    assert captured.out == ""


def test_system_writes_blue_prefix_to_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    default.system("hello")
    captured = capsys.readouterr()
    assert captured.out == f"{painted('[ System ] hello', 'dark_grey')}\n"
    assert captured.err == ""


def test_empty_message_is_silent(capsys: pytest.CaptureFixture[str]) -> None:
    default.info("   ")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
