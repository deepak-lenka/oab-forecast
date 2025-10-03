# OAB-Forecast Integration Plan

This document outlines the step-by-step plan to completely transform the codebase into OAB-forecast, integrating Chronos/AutoGluon models and adapting it to work with parquet files as the primary data source. The rebranding will be comprehensive, with no references to "timecopilot" remaining in any commands, documentation, or code.

## Repository Analysis Summary

OABForecast is a forecasting agent that combines LLM reasoning with statistical, ML, neural, and foundation models. The architecture follows a consistent workflow:

1. **Data ingestion & parameter setup**
2. **Feature analysis** (via tsfeatures)
3. **Model selection & cross-validation**
4. **Forecast generation**
5. **Anomaly detection**
6. **Explanation & delivery**

## Integration Plan

### 1. Package Rebranding & Structure Setup
- [ ] Fork/clone the OABForecast repository
- [x] Update `pyproject.toml` with new package name, description, and entry points
  ```toml
  [project]
  name = "oabforecast"
  description = "OAB-forecast: Time series forecasting with foundation models and LLM guidance"
  # ...
  
  [project.scripts]
  oabforecast = "oabforecast._cli:main"
  ```
- [ ] Rename the top-level package directory to `oabforecast/`
- [ ] Update imports throughout the codebase to reference `oabforecast` instead of `timecopilot`
- [x] Update README.md with OAB-forecast branding and examples

### 2. Parquet-First Data Handling
- [ ] Enhance `ExperimentDatasetParser.read_df` to prioritize parquet handling
  ```python
  # Location: oabforecast/utils/experiment_handler.py
  ```
- [ ] Add custom data cleaning and preprocessing logic for OAB-specific datasets
- [ ] Extend `ExperimentDataset` to support additional metadata from parquet sources
- [x] Update CLI documentation to highlight parquet file support
- [ ] Add examples showing the expected parquet schema/layout

### 3. Model Integration
- [ ] Review existing Chronos implementation in `oabforecast/models/foundation/chronos.py`
- [ ] Create new `AutoGluonForecaster` class in `oabforecast/models/autogluon.py`
  ```python
  # Template structure:
  from ..utils.forecaster import Forecaster
  
  class AutoGluonForecaster(Forecaster):
      def __init__(self, ...):
          self.alias = "AutoGluon"
          # ...
      
      def forecast(self, df, h, freq=None, level=None, quantiles=None):
          # Implementation here
          # Must return DataFrame with columns: unique_id, ds, self.alias, ...
  ```
- [ ] Add both models to `DEFAULT_MODELS` in `oabforecast/agent.py`
- [ ] Add necessary dependencies to `pyproject.toml`
- [ ] Create tests for the AutoGluon integration

### 4. Terminal UX for Drag-and-Drop
- [x] Verify the existing file path extraction in `_cli.py` works with dragged files
- [ ] Enhance the welcome message to explicitly mention drag-and-drop support
- [x] Update all terminal prompts and messages to use "OAB-forecast" branding
- [ ] Test the drag-and-drop workflow with both CSV and parquet files
- [ ] Add support for additional file formats if needed

### 5. Agent Workflow Customization
- [ ] Review and potentially customize the agent system prompt in `oabforecast/agent.py`
- [ ] Extend `ForecastAgentOutput` with OAB-specific fields or insights
- [ ] Customize the prettify method to highlight OAB-relevant metrics
- [ ] Consider adding custom evaluation metrics beyond MASE if needed

### 6. CLI Enhancement
- [x] Update the CLI entry point to use `oabforecast` name
- [ ] Add OAB-specific command-line options if needed
- [x] Update help text and examples to reflect OAB use cases
- [ ] Consider adding a dedicated subcommand for data cleaning/preparation

### 7. Testing & Validation
- [ ] Update existing tests to use the new package name
- [ ] Add integration tests for the new models and data handling
- [ ] Test the CLI with various input formats (CSV, parquet)
- [ ] Validate both installation methods:
  ```bash
  pip install oabforecast
  uvx add oabforecast
  ```

### 8. Documentation
- [ ] Update all documentation to reflect OAB-forecast branding
- [ ] Add examples specific to OAB use cases
- [ ] Document the parquet schema expectations
- [ ] Create a migration guide for existing OABForecast users

### 9. Distribution
- [ ] Finalize `pyproject.toml` with all dependencies
- [ ] Create a build and test it locally
- [ ] Publish to PyPI or your private package index
- [ ] Create a release with documentation

## Implementation Notes

### Data Flow
The existing data flow will be preserved:
1. Input data (now prioritizing parquet) → ExperimentDatasetParser
2. Feature extraction via tsfeatures_tool
3. Model selection via cross_validation_tool
4. Forecast generation with the best model
5. Anomaly detection
6. Structured output and visualization

### Key Files to Modify
- `pyproject.toml` - Package metadata and dependencies
- `oabforecast/_cli.py` (renamed from `oabforecast/_cli.py`) - CLI entry point
- `oabforecast/agent.py` - Agent orchestration and model selection
- `oabforecast/utils/experiment_handler.py` - Data parsing and experiment setup
- `oabforecast/models/` - Add AutoGluon implementation

### Drag-and-Drop Terminal Usage
The existing implementation already supports detecting file paths in user input. When a user drags a file into the terminal:

1. The shell inserts the absolute path to the file
2. The `_extract_file_path` helper in the CLI code detects this path
3. `ExperimentDatasetParser` loads and processes the file
4. The agent runs the full forecasting pipeline

No additional code is needed for basic drag-and-drop support, but the welcome message and documentation should be updated to make this capability more obvious to users.

## Conclusion

By following this integration plan, you'll transform the codebase into OAB-forecast while preserving the core architecture and workflow. The resulting package will support parquet files as first-class citizens, include Chronos and AutoGluon models, and maintain the intuitive terminal interface with drag-and-drop support.
