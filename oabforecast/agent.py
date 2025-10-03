# Re-export OAB-forecast agent API over current implementation
from timecopilot.agent import (  # type: ignore
    TimeCopilot as _TimeCopilot,
    AsyncTimeCopilot as _AsyncTimeCopilot,
    ForecastAgentOutput as _ForecastAgentOutput,
)

# Public OAB-forecast API
OABForecast = _TimeCopilot
AsyncOABForecast = _AsyncTimeCopilot
ForecastAgentOutput = _ForecastAgentOutput

__all__ = [
    "OABForecast",
    "AsyncOABForecast",
    "ForecastAgentOutput",
]
