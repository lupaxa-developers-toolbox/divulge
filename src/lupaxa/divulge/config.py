"""Configuration structures and defaults."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S %z"


@dataclass
class DivulgeConfig:
    error_colour: str = "light_red"
    error_prefix: str = "[ Error ]"
    warning_colour: str = "light_yellow"
    warning_prefix: str = "[ Warning ]"
    success_colour: str = "light_green"
    success_prefix: str = "[ Success ]"
    info_colour: str = "light_cyan"
    info_prefix: str = "[ Info ]"
    system_colour: str = "dark_grey"
    system_prefix: str = "[ System ]"
    use_colours: bool = True
    use_prefixes: bool = True
    use_bold: bool = False
    time_format: str = DEFAULT_TIME_FORMAT

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
