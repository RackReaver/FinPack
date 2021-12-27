"""Bring data in from CSV file.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

import csv
import logging
import os

from finpack.core.exceptions import DataError
from finpack.core.models import Account, Category, File, SubCategory


def loader(filepath, date):
    """Import chart of accounts from CSV file.

    args:
        filepath (str): Location of CSV file.

    return (dict): Account classes
    """
    logging.info("Running finpack.core.loader:loader")
    file = File(os.path.basename(filepath))

    with open(filepath, "r") as openFile:
        logging.debug("Looping through rows in CSV file.")
        for num, row in enumerate(csv.DictReader(openFile)):
            if row["name"] == "" or row["type"] == "":
                logging.debug(f"Skipping row {num} because name or type was blank.")
                break

            if file.check(row["name"], row["type"]):
                raise DataError(
                    f"Account names must be unique if same type, '{row['name']}' is duplicated."
                )

            ignore = ["name", "type", "category", "sub_category", "description"]
            history_data = []
            for x in row.items():
                if x[0] not in ignore and x[1].replace(" ", "") != "":
                    history_data.append([x[0], x[1].replace(",", "")])

            if history_data:
                acct = Account(
                    name=row["name"],
                    description=row["description"],
                    history=history_data,
                )
                sub_cat = SubCategory(row["sub_category"])
                sub_cat.add(acct)
                cat = Category(row["category"])
                cat.add(sub_cat)
                file.add(cat, row["type"])
    file.calculate(date)
    logging.info("Completed running finpack.core.loader:loader")
    from pprint import pprint

    return file
