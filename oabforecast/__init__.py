"""Top-level OAB-forecast package.

This module re-exports the public OAB-forecast API by importing from the
bundled `timecopilot` package included in this distribution.
"""

from __future__ import annotations

# Re-export from the bundled timecopilot package
from timecopilot import (  # noqa: F401
    TimeCopilot as OABForecast,
    AsyncTimeCopilot as AsyncOABForecast,
    TimeCopilotForecaster as OABForecastForecaster,
)

__all__ = [
    "OABForecast",
    "AsyncOABForecast",
    "OABForecastForecaster",
]
