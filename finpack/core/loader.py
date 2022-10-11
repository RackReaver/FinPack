"""Bring data in from CSV file.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

import csv
import logging
from typing import List

from finpack.core.exceptions import DataError
from finpack.core.models import Account


def loader(filepath: str) -> List[Account]:
    """Import chart of accounts from CSV file.

    args:
        filepath (str): Location of CSV file.

    return (list): Account classes
    """
    logging.info("Running finpack.core.loader:loader")
    accounts = []

    with open(filepath, "r") as openFile:
        logging.debug("Looping through rows in CSV file.")
        for num, row in enumerate(csv.DictReader(openFile)):
            if row["name"] == "" or row["group"] == "":
                logging.debug(f"Skipping row {num} because name or group was blank.")
                break
            if " ".join([row["group"], row["name"]]) in accounts:
                raise DataError(
                    "Account names must be unique if same group, '{}' is duplicated.".format(
                        row["name"]
                    )
                )

            ignore = ["name", "group", "category", "sub_category", "description"]
            data = []
            for x in row.items():
                if x[0] not in ignore and x[1].replace(" ", "") is not "":
                    data.append([x[0], x[1].replace(",", "")])

            if data:
                accounts.append(
                    Account(
                        name=row["name"],
                        group=row["group"],
                        category=row["category"],
                        sub_category=row["sub_category"],
                        description=row["description"],
                        history=data,
                    )
                )
    logging.info("Completed running finpack.core.loader:loader")
    return accounts
