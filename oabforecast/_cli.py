"""CLI wrapper for OAB-forecast.

This forwards the `oabforecast` console script to the internal implementation
under the bundled `timecopilot` package included in this project.
"""

from timecopilot._cli import main as _main


def main() -> None:
    _main()
