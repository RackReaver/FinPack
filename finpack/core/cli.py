"""
  ______ _       _____           _
 |  ____(_)     |  __ \\         | |
 | |__   _ _ __ | |__) |_ _  ___| | __
 |  __| | | '_ \\|  ___/ _` |/ __| |/ /
 | |    | | | | | |  | (_| | (__|   <
 |_|    |_|_| |_|_|   \\__,_|\\___|_|\\_\\

Super simple personal finance tracking/management tools.

Commands:
    init        Generate boilerplate data.csv
    balsheet    Outputs balance sheet to terminal

Usage:
    finpack init [--filepath=filepath] [--sample-dataset] [--overwrite]
    finpack balsheet [--filepath=filepath] [--levels=level] [--date=date]
    finpack (--version | --help | -h)

Options:
    --filepath=filepath         Location of the account list. [default: data.csv]
    --levels=level              How deep of a breakdown on the report [default: 3]
                                    1 Categories
                                    2 Categories + Sub-categories
                                    3 Categories + Sub-categories + accounts
    --overwrite                 Write over existing file
    --date=date                 Custom date to build report (YYYY-MM-DD) [default: today]
    -v --version                Display installed version
    -h --help                   Show available commands
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"

from datetime import datetime
from importlib import metadata

from docopt import docopt

from finpack.core import exceptions, init, loader
from finpack.reports import balsheet


def main():
    args = docopt(__doc__, version=metadata.version("finpack"))

    if args["init"]:
        init.init(
            args["--filepath"],
            sample_dataset=args["--sample-dataset"],
            force_overwrite=args["--overwrite"],
        )
    elif args["balsheet"]:
        data = loader.loader(args["--filepath"])

        # Convert str to datetime
        if args["--date"] == "today":
            balsheet_date = datetime.now()
        else:
            try:
                balsheet_date = datetime.strptime(args["--date"], "%Y-%m-%d")
            except TypeError:
                raise exceptions.DataError(
                    "Date format is incorrect, please use YYYY-MM-DD. For more information see the documentation."
                )

        print(
            balsheet.BalanceSheet(data).build(
                balsheet_date, levels=int(args["--levels"])
            )
        )
