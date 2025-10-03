# OAB-forecast Models & Methodology

## Available Models

OAB-forecast includes multiple model categories for time series forecasting:

### Foundation Models
- **Chronos** - Amazon's time series foundation model
- **TimesFM** - Google's time series foundation model
- **Toto** - Time series foundation model
- **Moirai** - Foundation model for time series
- **Sundial** - Time series foundation model
- **TimeGPT** - Nixtla's time series foundation model
- **TiRex** - Time series foundation model
- **TabPFN** - Tabular Prior-Data Fitted Networks

### Statistical & Classical Models
- **ADIDA** - Aggregation-Disaggregation Intermittent Demand Approach
- **AutoARIMA** - Automated ARIMA modeling
- **AutoCES** - Complex Exponential Smoothing
- **AutoETS** - Exponential Smoothing State Space Model
- **CrostonClassic** - Intermittent demand forecasting
- **DynamicOptimizedTheta** - Dynamic Theta model
- **HistoricAverage** - Simple historical average
- **IMAPA** - Intermittent demand forecasting
- **SeasonalNaive** - Seasonal naive forecast
- **Theta** - Theta method
- **ZeroModel** - Zero forecast baseline

### Other Models
- **Prophet** - Facebook's decomposable forecasting model
- **AutoLGBM** - LightGBM-based machine learning forecaster
- **Neural Network Models** - AutoNHITS and AutoTFT

## Default Models

By default, OAB-forecast uses these models for forecasting:

```python
DEFAULT_MODELS = [
    ADIDA(),
    AutoARIMA(),
    AutoCES(),
    AutoETS(),
    CrostonClassic(),
    DynamicOptimizedTheta(),
    HistoricAverage(),
    IMAPA(),
    SeasonalNaive(),
    Theta(),
    ZeroModel(),
    Prophet(),
]
```

## How to Specify Models

### CLI Method
```bash
# Use specific models via query
uv run -- oabforecast forecast data.csv --query "Use only AutoARIMA and Prophet models"

# Use foundation models
uv run -- oabforecast forecast data.csv --query "Try Chronos and TimesFM models"
```

### Programmatic Method
```python
from oabforecast import OABForecast
from timecopilot.models.stats import AutoARIMA
from timecopilot.models.prophet import Prophet
from timecopilot.models.foundation.chronos import Chronos

# Specify exactly which models to use
models = [
    AutoARIMA(),
    Prophet(),
    Chronos(context_length=512),
]

# Initialize agent with specific models
agent = OABForecast(
    llm="openai:gpt-4o-mini",
    forecasters=models,  # Only use these models
)
```

## Train/Test Split Methodology

OAB-forecast uses time series cross-validation with expanding windows:

1. **Multiple cutoff points** are created in the time series
2. For each cutoff:
   - **Training data**: All data points before the cutoff
   - **Test data**: The forecast horizon (h) periods after the cutoff
3. **Evaluation**: Models are evaluated using MASE (Mean Absolute Scaled Error)
4. **Selection**: The model with the lowest average MASE across all windows is selected

This approach:
- Respects temporal order (no data leakage)
- Mimics real forecasting scenarios
- Provides robust performance estimates
- Uses training data to scale errors for fair comparison

## Model Selection Process

1. **Feature extraction**: Compute time series features (trend, seasonality, stationarity)
2. **Cross-validation**: Test multiple models using the methodology above
3. **Comparison**: Compare models based on MASE scores
4. **Selection**: Choose the model with the lowest MASE
5. **Final forecast**: Generate the forecast using the selected model
6. **Anomaly detection**: Use the selected model to detect anomalies

The LLM agent explains the rationale for model selection based on the features and performance metrics.
