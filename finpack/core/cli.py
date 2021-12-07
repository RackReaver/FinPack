"""
  ______ _       _____           _
 |  ____(_)     |  __ \         | |
 | |__   _ _ __ | |__) |_ _  ___| | __
 |  __| | | '_ \|  ___/ _` |/ __| |/ /
 | |    | | | | | |  | (_| | (__|   <
 |_|    |_|_| |_|_|   \__,_|\___|_|\_\\

Super simple personal finance tracking/management tools.

Commands:
    init        Generate sample accounts.yaml file
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

from docopt import docopt
from importlib import metadata

from finpack.core import init, loader
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

        print(
            balsheet.BalanceSheet(data).build(
                args["--date"], levels=int(args["--levels"])
            )
        )
