import unittest
from datetime import datetime

from finpack.core import Account, AccountError, DataError

NAME = "The only Checking Account you will ever need"
TYPE = "asset"
CATEGORY = "Cash and Cash Equivalents"
SUB_CATEGORY = "Checking Accounts"
DESCRIPTION = "Description for checking account 1"
HISTORY = [["2021-01-01", "1000.00"], ["2021-12-01", "2000.00"]]


class TestCore(unittest.TestCase):
    def setUp(self):
        self.account = Account(
            NAME,
            TYPE,
            CATEGORY,
            SUB_CATEGORY,
            DESCRIPTION,
            HISTORY,
        )

    def test_account_name(self):
        self.assertEqual(self.account.name, NAME)

    def test_account_short_name(self):
        self.assertEqual(self.account.short_name, NAME[:37] + "...")

    def test_account_type(self):
        self.assertEqual(self.account.type, TYPE)

    def test_account_category(self):
        self.assertEqual(self.account.category, CATEGORY)

    def test_account_sub_category(self):
        self.assertEqual(self.account.sub_category, SUB_CATEGORY)

    def test_account_description(self):
        self.assertEqual(self.account.description, DESCRIPTION)

    def test_account_history(self):
        self.assertEqual(self.account.history, HISTORY)

    def test_repr(self):
        self.assertEqual(
            str(self.account),
            "<Account.asset.The-only-Checking-Account-you-will-ever-need>",
        )

    def test_eq(self):
        self.assertTrue(self.account == TYPE.lower() + " " + NAME)

    def test_current_value(self):
        self.assertEqual(self.account.current_value(), "2000.00")

    def test_add_value(self):
        temp = self.account.add_value(3000, date=datetime(2021, 2, 1))
        self.assertTrue(temp, True)

    def test_add_value2(self):
        # Test 'value' DataError
        with self.assertRaises(DataError):
            self.account.add_value("abc", date=datetime(2021, 2, 1))

    def test_add_value3(self):
        # Test 'date' DataError
        with self.assertRaises(DataError):
            self.account.add_value(3000, date="2021-02-01")

    def test_add_value4(self):
        # Test AccountError
        with self.assertRaises(AccountError):
            self.account.add_value(3000, date=datetime(2021, 1, 1))


# if __name__ == "__main__":
#     unittest.main()
