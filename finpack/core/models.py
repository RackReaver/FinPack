"""Package specific models.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

from dataclasses import dataclass, field
from datetime import datetime
from os import stat

from finpack.core.exceptions import AccountError, DataError


class Account:
    def __init__(self, name, description, history):
        self.name = name
        self.short_name = name[:40]
        self.description = description
        self.history = history

        if len(self.name) > 40:
            self.short_name = name[:37] + "..."

    def __repr__(self):
        return self.name

    def value(self, date):
        """Get latest monetary value of account.

        args:
            date (datetime): [default: None] As of date to get account value.

        return (float): Monetary value
        """
        for val in self.history:
            if val[0] <= date.strftime("%Y-%m-%d"):
                value = val

        return float(value[1])

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


@dataclass
class SubCategory:
    name: str
    current_value: float = 0.00
    current_percentage_value: int = field(default=0, repr=False)
    value: float = field(default=0.00, repr=False)
    percentage_value: int = field(default=0, repr=False)
    accounts: list = field(init=False, default_factory=list, repr=False)

    def __iter__(self):
        return iter(self.accounts)

    def add(self, account: Account):
        self.accounts.append(account)
        self.current_value += round(account.value(datetime.now()), 2)
        return True


@dataclass
class Category:
    name: str
    current_value: float = 0.00
    current_percentage_value: int = field(default=0, repr=False)
    value: float = field(default=0.00, repr=False)
    percentage_value: int = field(default=0, repr=False)
    sub_categories: list = field(init=False, default_factory=list, repr=False)

    def __str__(self):
        return self.name

    def __iter__(self):
        return iter(self.sub_categories)

    def add(self, sub_category: SubCategory):
        self.sub_categories.append(sub_category)
        self.current_value += round(sub_category.current_value, 2)
        return True


@dataclass
class RootType:
    current_value: float = 0.00
    current_percentage_value: int = field(default=0, repr=False)
    value: float = field(default=0.00, repr=False)
    percentage_value: int = field(default=0, repr=False)
    categories: list = field(init=False, default_factory=list, repr=False)

    def __iter__(self):
        return iter(self.categories)

    def add(self, category: Category):
        self.categories.append(category)
        self.current_value += round(category.current_value, 2)


@dataclass
class File:
    filename: str
    data: dict = field(init=False, repr=False)

    def __post_init__(self):
        self.data = {
            "assets": RootType(),
            "liabilities": RootType(),
            "incomes": RootType(),
            "expenses": RootType(),
        }

    def __getitem__(self, key):
        return self.data[self._pluralize(key)]

    @staticmethod
    def _pluralize(root_type):
        if root_type == "asset":
            return "assets"
        if root_type == "liability":
            return "liabilities"
        if root_type == "income":
            return "incomes"
        if root_type == "expense":
            return "expenses"
        else:
            raise DataError(f"Unable to pluralize '{root_type}'")

    def check(self, name: str, root_type: str):
        for cat in self.data[self._pluralize(root_type)]:
            for sub_cat in cat:
                if name in sub_cat:
                    return True
        return False

    def add(self, category: Category, root_type: str):
        self.data[self._pluralize(root_type)].add(category)

    def calculate(self, date):
        # TODO: This function should compute and populate:
        # - current_percentage_value
        # - value
        # - percentage_value
        pass
