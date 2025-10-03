# Re-export OAB-forecast forecaster API over current implementation
from timecopilot.forecaster import (  # type: ignore
    TimeCopilotForecaster as _TimeCopilotForecaster,
)

OABForecastForecaster = _TimeCopilotForecaster

__all__ = [
    "OABForecastForecaster",
]
