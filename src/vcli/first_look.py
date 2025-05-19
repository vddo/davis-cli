import csv
import pathlib


"""Check data before import"""


class FirstLook:
    """First exploration of the raw data.
    Focus on finding issues that would prevent the import to a pandas DataFrame."""

    def __init__(self, path: pathlib.Path) -> None:
        self.header = self.get_columns(path)

    def get_columns(self, path: pathlib.Path) -> list:
        """Gets a list of columns"""
        with open(path) as f:
            reader = csv.reader(f)
            print(next(reader))
            return []

    def get_columns_count(self) -> int:
        """Get count of columns"""
        return len(self.header)
