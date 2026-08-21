"""Reset the shared engine between tests."""

from __future__ import annotations

from collections.abc import Iterator

import pytest


@pytest.fixture(autouse=True)
def reset_engine() -> Iterator[None]:
    from lupaxa.divulge.config import DivulgeConfig
    from lupaxa.divulge.engine import default

    default._config = DivulgeConfig()
    yield
    default._config = DivulgeConfig()
