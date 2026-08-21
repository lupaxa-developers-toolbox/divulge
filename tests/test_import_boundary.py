"""Library-only package boundary."""

from __future__ import annotations

import pathlib
import runpy

import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = REPO_ROOT / "src" / "lupaxa" / "divulge"


def test_namespace_package_has_no_init() -> None:
    assert not (REPO_ROOT / "src" / "lupaxa" / "__init__.py").is_file()


def test_no_package_cli_or_main_module() -> None:
    assert not (PKG / "cli.py").is_file()
    assert not (PKG / "__main__.py").is_file()


def test_package_is_not_runnable_as_module() -> None:
    with pytest.raises(ImportError):
        runpy.run_module("lupaxa.divulge", run_name="__main__")


def test_public_all_excludes_engine_and_core() -> None:
    import lupaxa.divulge as divulge

    assert "CoreDivulge" not in divulge.__all__
    assert "Engine" not in divulge.__all__
    assert "default" not in divulge.__all__


def test_no_repo_root_cli() -> None:
    assert not (REPO_ROOT / "cli.py").is_file()
    assert not (REPO_ROOT / "setup.cfg").is_file()
