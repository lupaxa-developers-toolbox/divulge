"""Private printer engine and the shared default instance."""

from __future__ import annotations

import pprint
import sys
from dataclasses import replace
from datetime import datetime
from typing import Any, TextIO

from termcolor import COLORS, colored

from .config import DEFAULT_TIME_FORMAT, DivulgeConfig


class Engine:
    """Console printer used by the package-level functions and wrapper."""

    def __init__(self, options: dict[str, Any] | None = None) -> None:
        base_cfg = DivulgeConfig()
        if options:
            self._config = self._merge_into_config(base_cfg, options)
        else:
            self._config = base_cfg

    def configure(self, **options: Any) -> None:
        self._config = self._merge_into_config(self._config, options)

    def error(self, message: Any, **options: Any) -> None:
        self._show_with_level("error", message, options, stream=sys.stderr)

    def warning(self, message: Any, **options: Any) -> None:
        self._show_with_level("warning", message, options, stream=sys.stderr)

    def success(self, message: Any, **options: Any) -> None:
        self._show_with_level("success", message, options, stream=sys.stdout)

    def info(self, message: Any, **options: Any) -> None:
        self._show_with_level("info", message, options, stream=sys.stdout)

    def system(self, message: Any, **options: Any) -> None:
        self._show_with_level("system", message, options, stream=sys.stdout)

    warn = warning
    ok = success

    def _show_with_level(
        self,
        level: str,
        message: Any,
        options: dict[str, Any],
        stream: TextIO,
    ) -> None:
        colour_key = f"{level}_colour"
        prefix_key = f"{level}_prefix"
        settings = self._build_settings(options, colour_key, prefix_key)
        text = self._coerce_message(message, settings["time_format"])
        if not text.strip():
            return
        if settings["use_prefixes"] and settings.get("prefix"):
            text = f"{settings['prefix']} {text}"
        colour = settings.get("colour")
        if settings["use_colours"] and colour in COLORS:
            attrs = ["bold"] if settings["use_bold"] else None
            text = colored(text, colour, attrs=attrs, force_color=True)
        print(text, file=stream)

    def _build_settings(
        self,
        call_options: dict[str, Any],
        colour_key: str,
        prefix_key: str,
    ) -> dict[str, Any]:
        merged: dict[str, Any] = {**self._config.as_dict(), **call_options}
        if "color" in merged and "colour" not in merged:
            merged["colour"] = merged.pop("color")
        if "colour" in merged and colour_key not in call_options:
            merged[colour_key] = merged["colour"]
        if "prefix" in merged and prefix_key not in call_options:
            merged[prefix_key] = merged["prefix"]
        return {
            "colour": merged.get(colour_key),
            "prefix": merged.get(prefix_key),
            "use_colours": bool(merged.get("use_colours", True)),
            "use_prefixes": bool(merged.get("use_prefixes", True)),
            "use_bold": bool(merged.get("use_bold", False)),
            "time_format": merged.get("time_format", DEFAULT_TIME_FORMAT),
        }

    def _coerce_message(self, message: Any, time_format: str) -> str:
        if isinstance(message, datetime):
            return message.strftime(time_format)
        if isinstance(message, str):
            return message
        return pprint.pformat(message, width=80, compact=True)

    @staticmethod
    def _merge_into_config(
        base_config: DivulgeConfig,
        updates: dict[str, Any],
    ) -> DivulgeConfig:
        allowed = base_config.as_dict()
        filtered = {key: value for key, value in updates.items() if key in allowed}
        return replace(base_config, **filtered)


default = Engine()
