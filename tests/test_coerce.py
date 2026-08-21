"""Message coercion for datetime and non-strings."""

from __future__ import annotations

from datetime import datetime

import pytest

from lupaxa.divulge.engine import default


def test_datetime_uses_time_format(capsys: pytest.CaptureFixture[str]) -> None:
    default.configure(use_colours=False, use_prefixes=False)
    default.info(datetime(2026, 8, 21, 14, 30, 0), time_format="%Y-%m-%d %H:%M:%S")
    captured = capsys.readouterr()
    assert captured.out == "2026-08-21 14:30:00\n"


def test_mapping_is_pformatted(capsys: pytest.CaptureFixture[str]) -> None:
    default.configure(use_colours=False, use_prefixes=False)
    default.info({"a": 1})
    captured = capsys.readouterr()
    assert captured.out == "{'a': 1}\n"
