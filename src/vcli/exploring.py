import csv
import pathlib

import pandas as pd

"""Check data before import"""


class Explorer:
    """First exploration of the raw data.
    Focus on finding issues that would prevent the import to a pandas DataFrame."""

    def __init__(self, path: pathlib.Path, sep: str = ",") -> None:
        self.header = self.get_columns(path)
        self.count_columns = self.header.size
        self.mismatches = []

        self.go_explore(path, sep)

    def go_explore(self, path, sep: str):
        """Executes standard process"""
        idx = 0
        with open(path) as f:
            reader = csv.reader(f, delimiter=sep)
            for row in reader:
                len_vec = len(row)
                if len_vec != self.count_columns:
                    self.mismatches.append((idx, len_vec))
                idx += 1
        self.count_rows = idx + 1

        return

    def get_columns(self, path: pathlib.Path) -> pd.Series:
        """Gets a list of columns"""
        with open(path) as f:
            reader = csv.reader(f)
            return pd.Series(next(reader))

    def get_mismatches_stats(self) -> pd.DataFrame:
        return pd.DataFrame(
            self.mismatches, columns=["index_raw", "len_value_vec"]
        ).agg(
            {
                "index_raw": ["min", "max", "median"],
                "len_value_vec": ["min", "max", "median"],
            }
        )
