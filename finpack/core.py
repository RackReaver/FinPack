"""FinPack
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

import csv
from datetime import datetime

from finpack import utils
from finpack.reports.balsheet import BalanceSheet


class DataError(Exception):
    """Data not provided or available as expected."""

    pass


class AccountError(Exception):
    """Account class exception"""

    pass


class Account:
    def __init__(self, name, type, category, sub_category, description, history):
        self.name = name
        self.short_name = name[:40]
        self.type = type.lower()
        self.category = category
        self.sub_category = sub_category
        self.description = description
        self.history = history

        if len(self.name) > 40:
            self.short_name = name[:37] + "..."

    def __repr__(self):
        return "<Account." + self.type + "." + self.name.replace(" ", "-") + ">"

    def __eq__(self, other):
        return " ".join([self.type, self.name]) == other

    def current_value(self):
        """Get latest monetary value of account.

        return (str): Monetary value
        """
        first = True
        for val in self.history:
            if first == True:
                value = val
                first = False
            else:
                if val[0] > value[0]:
                    value = val

        return value[1]

    def add_value(self, value, date=datetime.now()):
        """

        args:
            value (int|float): Account value

        kwargs:
            date (datetime): date that is to be used

        return (bool): True/False based on success
        """

        # If type is int convert it to float
        if isinstance(value, int):
            value = float(value)

        # If 'value' type not float raise error
        if not isinstance(value, float):
            raise DataError(
                'Wrong variable type passed to function, "value" should be a float or int not {}'.format(
                    type(value).__name__
                )
            )
        # If type is not datetime raise error
        if not isinstance(date, datetime):
            raise DataError(
                'Wrong variable type passed to function, "date" should be a datetime not {}'.format(
                    type(date).__name__
                )
            )

        # Convert datetime to str
        date = date.strftime("%Y-%m-%d")

        # Verify date value does not exist
        if date not in [x[0] for x in self.history]:
            self.history.append([date, "{:.2f}".format(value)])

        else:
            # TODO: Prompt to overwrite and allow for auto overwrite.
            raise AccountError("Date value already exists")

        return True


def importer(filepath, header=True):
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


def balsheet(data, date, level):
    """Build balance sheet

    args:
        data (list): data from importer
        TODO: date (datetime): date in datetime format
        level (int):    1: Categories
                        2: Categories + Sub-categories
                        3: Categories + Sub-categories + accounts

    return (str): Balance Sheet
    """
    return BalanceSheet(data).build(levels=level)


def cashflow(data):
    """Build cashflow statement"""
    # TODO: Build Cash Flow Report Function
    pass


def allocation(data):
    """Build asset and liability allocation"""
    # TODO: Build Allocation Report Function
    pass
