import logging
import pathlib
import sys

import click
import pandas as pd
from icecream import ic

from src.vcli import exploring, read_csv, scatter_matrix, cleaning


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
    expl = exploring.Explorer(p)
    click.echo(
        f"The data set has {expl.count_columns} columns\n"
        + f"and {expl.count_rows} rows\n"
    )

    if get_header:
        click.echo(expl.header.to_string())

    click.echo(
        "Mismatching Rows\n"
        + "The following are stats of index and count of values for each rows that do not match with columns\n"
        + "The first data points starts with index 0\n"
    )
    click.echo(expl.get_mismatches_stats())


@vcli.command()
@click.argument("cleaner")
def clean(cleaner):
    """Chose a Cleaner [football] to clean the raw data set"""
    match cleaner.lower():
        case "football":
            cleaner = cleaning.FootballCleaner()


if __name__ == "__main__":
    vcli()
