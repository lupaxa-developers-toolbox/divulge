"""Package-level functions delegate to the shared engine."""

from __future__ import annotations

import pytest

import lupaxa.divulge as divulge
from tests.painted import painted


def test_module_system_and_info(capsys: pytest.CaptureFixture[str]) -> None:
    divulge.system("job")
    divulge.info("ok")
    captured = capsys.readouterr()
    assert captured.out == (
        f"{painted('[ System ] job', 'dark_grey')}\n{painted('[ Info ] ok', 'light_cyan')}\n"
    )


def test_module_configure_and_restore(capsys: pytest.CaptureFixture[str]) -> None:
    divulge.configure(use_colours=False, use_prefixes=False)
    divulge.info("plain")
    divulge.configure(use_colours=True, use_prefixes=True)
    divulge.info("pretty")
    captured = capsys.readouterr()
    assert captured.out == f"plain\n{painted('[ Info ] pretty', 'light_cyan')}\n"


@pytest.mark.parametrize(
    ("func_name", "prefix", "stream"),
    [
        ("info", "[ Info ]", "out"),
        ("success", "[ Success ]", "out"),
        ("warning", "[ Warning ]", "err"),
        ("error", "[ Error ]", "err"),
        ("system", "[ System ]", "out"),
    ],
)
def test_module_functions_use_default_prefix_and_stream(
    func_name: str,
    prefix: str,
    stream: str,
    capsys: pytest.CaptureFixture[str],
) -> None:
    getattr(divulge, func_name)("hello")
    captured = capsys.readouterr()
    written = captured.out if stream == "out" else captured.err
    silent = captured.err if stream == "out" else captured.out
    assert prefix in written
    assert "hello" in written
    assert silent == ""


def test_public_all_lists_documented_names() -> None:
    assert set(divulge.__all__) >= {
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
    }
    assert "CoreDivulge" not in divulge.__all__
    assert "Engine" not in divulge.__all__
