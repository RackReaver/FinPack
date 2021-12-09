"""Class for building custom balance sheets.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

from datetime import datetime

from finpack.utils import _add_char


class BalanceSheet:
    def __init__(self, data):
        self._data = data
        self.WIDTH = 70
        self.TAB = 5
        self.categories = self._build_categories(datetime.now())

    def _build_title(self, title, char="="):
        return "{0}\n{1}\n{0}".format(_add_char(self.WIDTH, char), title)

    def _build_categories(self, date):
        """Builds categories and category totals to sort accounts

        kwargs:
            date (datetime): As of date to building balance sheet.

        return (dict): Nested categories with type and value
        """
        cat = {}
        for acct in self._data:
            if acct.type == "asset" or acct.type == "liability":
                # Check if category has been added
                if acct.category not in cat:
                    cat[acct.category] = {
                        "type": acct.type,
                        "value": 0.00,
                        "sub_categories": {},
                    }
                # Check if sub_category has been added
                if acct.sub_category not in cat[acct.category]["sub_categories"]:
                    cat[acct.category]["sub_categories"][acct.sub_category] = 0.00

                # Add account value to category total value
                cat[acct.category]["value"] += float(acct.value(date))
                # Add account value to sub_category total value
                cat[acct.category]["sub_categories"][acct.sub_category] += float(
                    acct.value(date)
                )

                # Round category total value
                cat[acct.category]["value"] = round(cat[acct.category]["value"], 2)
                # Round sub_category total value
                cat[acct.category]["sub_categories"][acct.sub_category] = round(
                    cat[acct.category]["sub_categories"][acct.sub_category], 2
                )

        return cat

    def build(self, date, levels=3):
        """Build balance sheet

        args:
            date (datetime): As of date to building balance sheet.
        kwargs:
            level (int): [default: 3]
                    1: Categories
                    2: Categories + Sub-categories
                    3: Categories + Sub-categories + accounts

        return (str): Balance Sheet
        """
        # TODO: Dynamic tabbing needs to be added for levels 1 and 2. Not required for levels 3.
        data_export = {
            "assets": {"str": self._build_title("Assets"), "total": 0.00},
            "liabilities": {"str": self._build_title("Liabilities"), "total": 0.00},
            "net_worth": {"str": "", "total": 0.00},
        }

        categories = self._build_categories(date)

        # Loop through categories
        for cat, data in categories.items():

            value = "{:,.2f}".format(data["value"])
            calc = self.WIDTH - len(cat) - (self.TAB * 2) - len(value)

            if data["type"] == "asset":
                data_export["assets"]["total"] += data["value"]
                data_export["assets"]["str"] += "\n{}{}{}".format(
                    cat, _add_char(calc), value
                )
            elif data["type"] == "liability":
                data_export["liabilities"]["total"] += data["value"]
                data_export["liabilities"]["str"] += "\n{}{}{}".format(
                    cat, _add_char(calc), value
                )

            if levels >= 2:
                # Loop through sub_categories
                for s_cat, acct_value in data["sub_categories"].items():

                    value = "{:,.2f}".format(acct_value)
                    calc = (
                        self.WIDTH - self.TAB - len(s_cat) - self.TAB - len(str(value))
                    )

                    if data["type"] == "asset":
                        data_export["assets"]["str"] += "\n{}{}{}{}".format(
                            _add_char(self.TAB), s_cat, _add_char(calc), value
                        )
                    elif data["type"] == "liability":
                        data_export["liabilities"]["str"] += "\n{}{}{}{}".format(
                            _add_char(self.TAB), s_cat, _add_char(calc), value
                        )

                if levels >= 3:
                    # Looping through accounts
                    for account in self._data:
                        value = "{:,.2f}".format(float(account.value(date)))
                        calc = (
                            self.WIDTH
                            - (self.TAB * 2)
                            - len(account.short_name)
                            - len(str(value))
                        )
                        if account.type == "asset" and account.sub_category == s_cat:
                            data_export["assets"]["str"] += "\n{}{}{}{}".format(
                                _add_char(self.TAB * 2),
                                account.short_name,
                                _add_char(calc),
                                value,
                            )
                        elif (
                            account.type == "liability"
                            and account.sub_category == s_cat
                        ):
                            data_export["liabilities"]["str"] += "\n{}{}{}{}".format(
                                _add_char(self.TAB * 2),
                                account.short_name,
                                _add_char(calc),
                                value,
                            )

        total_asset_title = "OVERALL TOTAL ASSETS"
        value = "{:,.2f}".format(data_export["assets"]["total"])
        calc = self.WIDTH - len(total_asset_title) - len(str(value))
        data_export["assets"]["str"] += "\n{}{}{}".format(
            total_asset_title, _add_char(calc), value
        )

        total_liability_title = "OVERALL TOTAL LIABILITIES"
        value = "{:,.2f}".format(data_export["liabilities"]["total"])
        calc = self.WIDTH - len(total_liability_title) - len(str(value))
        data_export["liabilities"]["str"] += "\n{}{}{}".format(
            total_liability_title, _add_char(calc), value
        )

        net_worth_title = "NET WORTH"
        net_worth = "{:,.2f}".format(
            data_export["assets"]["total"] - data_export["liabilities"]["total"]
        )
        calc = self.WIDTH - len(net_worth_title) - len(net_worth)
        pre_build_net_worth_str = "{}{}{}".format(
            net_worth_title, _add_char(calc), net_worth
        )
        data_export["net_worth"]["str"] = self._build_title(pre_build_net_worth_str)
        data_export["net_worth"]["total"] = net_worth

        export_str = data_export["assets"]["str"] + "\n"
        export_str += data_export["liabilities"]["str"] + "\n"
        export_str += data_export["net_worth"]["str"]

        return export_str
