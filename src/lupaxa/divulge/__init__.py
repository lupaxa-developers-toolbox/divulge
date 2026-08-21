"""lupaxa.divulge — opinionated console messaging helper."""

from __future__ import annotations

from typing import Any

from .config import DEFAULT_TIME_FORMAT, DivulgeConfig
from .engine import default
from .version import __version__, get_version
from .wrapper import Divulge, divulge

__all__ = [
    "DEFAULT_TIME_FORMAT",
    "Divulge",
    "DivulgeConfig",
    "__version__",
    "configure",
    "divulge",
    "error",
    "get_version",
    "info",
    "success",
    "system",
    "warning",
]


def configure(**options: Any) -> None:
    default.configure(**options)


def error(message: Any, **options: Any) -> None:
    default.error(message, **options)


def warning(message: Any, **options: Any) -> None:
    default.warning(message, **options)


def success(message: Any, **options: Any) -> None:
    default.success(message, **options)


def info(message: Any, **options: Any) -> None:
    default.info(message, **options)


def system(message: Any, **options: Any) -> None:
    default.system(message, **options)
