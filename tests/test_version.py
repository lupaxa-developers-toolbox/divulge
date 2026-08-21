"""Package version metadata."""

from __future__ import annotations


def test_version_is_semver() -> None:
    from lupaxa.divulge import __version__, get_version

    assert __version__ == "0.0.0"
    assert get_version() == "0.0.0"
