"""Expected coloured text via termcolor (same settings as the engine)."""

from __future__ import annotations

from termcolor import colored


def painted(text: str, colour: str, *, bold: bool = False) -> str:
    attrs = ["bold"] if bold else None
    return colored(text, colour, attrs=attrs, force_color=True)
