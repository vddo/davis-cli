import csv
import pathlib

import pandas as pd

"""Check data before import"""


class Explorer:
    """First exploration of the raw data.
    Focus on finding issues that would prevent the import to a pandas DataFrame."""

    def __init__(self, path: pathlib.Path) -> None:
        self.header = self.get_columns(path)

    def get_columns(self, path: pathlib.Path) -> pd.Series:
        """Gets a list of columns"""
        with open(path) as f:
            reader = csv.reader(f)
            return pd.Series(next(reader))

    def get_columns_count(self) -> int:
        """Get count of columns"""
        return len(self.header)
