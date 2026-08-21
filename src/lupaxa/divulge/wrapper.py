"""Chainable wrapper around a single value."""

from __future__ import annotations

from typing import Any

from .engine import default


class Divulge:
    """Chainable wrapper: ``Divulge("hello").info().success()``."""

    def __init__(self, value: Any) -> None:
        self.value = value

    def info(self, **options: Any) -> Divulge:
        default.info(self.value, **options)
        return self

    def error(self, **options: Any) -> Divulge:
        default.error(self.value, **options)
        return self

    def warning(self, **options: Any) -> Divulge:
        default.warning(self.value, **options)
        return self

    def success(self, **options: Any) -> Divulge:
        default.success(self.value, **options)
        return self

    def system(self, **options: Any) -> Divulge:
        default.system(self.value, **options)
        return self

    warn = warning
    ok = success


def divulge(value: Any) -> Divulge:
    """Sugar helper that returns a ``Divulge`` wrapper."""
    return Divulge(value)
