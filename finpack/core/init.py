"""Build boilerplate with or without sample dataset.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"

import os
from datetime import datetime


def init(filepath="data.csv", sample_dataset=False, force_overwrite=False):
    """Build boilerplate with or without sample dataset.

    args:
        filepath (str): Location and name of file.
    kwargs:
        sample_dataset (bool): If sample data should be included.
        force_overwrite (bool): If true, don't prompt before overwriting file.

    return (bool): True if created successfully.
    """
    filepath = str(filepath).replace("\\", "/").strip()

    data = "name,type,category,sub_category,description,{}".format(
        datetime.now().strftime("%Y-%m-%d")
    )

    if sample_dataset == True:
        data += "\nChecking Account 1,asset,Cash and Cash Equivalents,Checking Accounts,,1000.00"
        data += "\nChecking Account 2,asset,Cash and Cash Equivalents,Checking Accounts,,2000.00"
        data += "\nSavings Account 1,asset,Cash and Cash Equivalents,Savings Accounts,,5000.00"
        data += (
            "\nRetirement Savings Account,asset,Retirement Accounts,401(k)s,,20000.00"
        )
        data += "\n123 Main St.,asset,Property,Real Estate,,200000.00"
        data += "\n123 Main St.,liability,Loans and Mortgages,Mortgages,,150000.00"
        data += "\nStudent Loan 1,liability,Loans and Mortgages,Student Loans,,10000.00"
        data += "\nStudent Loan 2,liability,Loans and Mortgages,Student Loans,,10000.00"

    def write_file():
        with open(filepath, "w") as openfile:
            openfile.write(data)

    if not os.path.isfile(filepath) or force_overwrite == True:
        write_file()
    else:
        while True:
            user_input = input("File already exists, overwrite it (y/n)? ")
            if user_input == "Y" or user_input == "y":
                write_file()
                break
            if user_input == "N" or user_input == "n":
                break
