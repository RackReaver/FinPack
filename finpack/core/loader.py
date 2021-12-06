"""Bring data in from CSV file.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

import csv

from finpack.core.exceptions import DataError
from finpack.core.models import Account


def loader(filepath, header=True):
    """Import chart of accounts from CSV file.

    args:
        filepath (str): Location of CSV file.
    kwargs:
        header (bool): If column names are included in file.

    return (dict):
    """
    accounts = []

    with open(filepath, "r") as openFile:
        r = csv.DictReader(openFile)
        # Loop through all rows
        for row in r:

            # Skip row if name and type are blank
            if row["name"] == "" and row["type"] == "":
                break

            # Check if account name already exists
            if " ".join([row["type"], row["name"]]) in accounts:
                raise DataError(
                    "Account names must be unique if same type, '{}' is duplicated.".format(
                        row["name"]
                    )
                )

            ignore = ["name", "type", "category", "sub_category", "description"]
            # Parse out only financial data
            data = [
                [x[0], x[1].replace(",", "")] for x in row.items() if x[0] not in ignore
            ]

            # Add account to accounts list
            accounts.append(
                Account(
                    name=row["name"],
                    type=row["type"],
                    category=row["category"],
                    sub_category=row["sub_category"],
                    description=row["description"],
                    history=data,
                )
            )

    return accounts
