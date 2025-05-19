import pandas as pd
from pathlib import Path


def read_csv(p: Path, sep: str = ",", decimal: str = ".") -> pd.DataFrame:
    """Reads a csv file

    Args:
        p (Path): Path object representing the csv file
        sep (str), default ",": Character as a delimiter
        decimal (str), default ".": Character as decimal

    Returns:
        A pd.DataFrame
    """
    return pd.read_csv(filepath_or_buffer=p, sep=sep, decimal=decimal)
