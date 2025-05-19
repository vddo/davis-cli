import logging
import pathlib
import sys

import click
import pandas as pd
from icecream import ic

from src.vcli import first_look, read_csv, scatter_matrix, cleaning


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
@click.option("--get-header", is_flag=True)
@click.argument("path")
def look(path, get_header) -> None:
    """Have a first look at the raw data"""
    click.echo("Having a first look around\n")
    p = pathlib.Path(path)
    fl = first_look.FirstLook(p)
    click.echo(f"The data set has {fl.get_columns_count()} columns")

    if get_header:
        click.echo(fl.header.to_string())


@vcli.command()
@click.argument("cleaner")
def clean(cleaner):
    """Chose a Cleaner [football] to clean the raw data set"""
    match cleaner.lower():
        case "football":
            cleaner = cleaning.FootballCleaner()


if __name__ == "__main__":
    vcli()
