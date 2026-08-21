"""DivulgeConfig defaults including the system level."""

from __future__ import annotations


def test_system_defaults_and_as_dict() -> None:
    from lupaxa.divulge.config import DEFAULT_TIME_FORMAT, DivulgeConfig

    cfg = DivulgeConfig()
    data = cfg.as_dict()
    assert cfg.system_colour == "dark_grey"
    assert cfg.system_prefix == "[ System ]"
    assert data["system_colour"] == "dark_grey"
    assert data["system_prefix"] == "[ System ]"
    assert data["error_prefix"] == "[ Error ]"
    assert data["warning_prefix"] == "[ Warning ]"
    assert data["success_prefix"] == "[ Success ]"
    assert data["info_prefix"] == "[ Info ]"
    assert data["use_colours"] is True
    assert data["use_prefixes"] is True
    assert data["use_bold"] is False
    assert data["time_format"] == DEFAULT_TIME_FORMAT
    assert DEFAULT_TIME_FORMAT == "%Y-%m-%d %H:%M:%S %z"
