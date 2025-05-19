import logging
import pathlib
import sys

import click
from icecream import ic

from src.vcli import read_csv, scatter_matrix, first_look


@click.group()
def vcli():
    pass


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 main.py [option] my-csv-file.csv")
        return

    p = pathlib.Path(sys.argv[1])
    if not p.is_file():
        logging.error("Not a file")
        return

    data = read_csv.read_csv(p)
    ic(data)


@vcli.command()
@click.argument("path")
def look(path) -> None:
    """Have a first look at the raw data"""
    click.echo("Having a first look around")
    p = pathlib.Path(path)
    first_look.FirstLook(p)


if __name__ == "__main__":
    vcli()
