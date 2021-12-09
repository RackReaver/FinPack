"""Package specific models.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

from datetime import datetime

from finpack.core.exceptions import AccountError, DataError


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

    def value(self, date):
        """Get latest monetary value of account.

        args:
            date (datetime): [default: None] As of date to get account value.

        return (str): Monetary value
        """
        for val in self.history:
            if val[0] <= date.strftime("%Y-%m-%d"):
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
            self.history.sort()

        else:
            # TODO: Prompt to overwrite and allow for auto overwrite.
            raise AccountError("Date value already exists")

        return True
