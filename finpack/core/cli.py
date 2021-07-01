"""
  ______ _       _____           _
 |  ____(_)     |  __ \         | |
 | |__   _ _ __ | |__) |_ _  ___| | __
 |  __| | | '_ \|  ___/ _` |/ __| |/ /
 | |    | | | | | |  | (_| | (__|   <
 |_|    |_|_| |_|_|   \__,_|\___|_|\_\\

Super simple financial tracking/management tools.

Commands:
  init  Build sample accounts.yaml file
  run   Update account values interactively

Usage:
    finpack init [--filepath=filename] [--overwrite]
    finpack run [--filepath=filename] [--date=date]

Options:
    --filepath=filename        Location of the account list [default: accounts.yaml]
    --date=date                Custom date to run against (YYYY-MM-DD). [default: today]
    --overwrite                Write over existing file
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

import os
from datetime import datetime

import yaml
from docopt import docopt

from finpack.core import app


# Required to add proper yaml list indentation. Issue for this is still open.
# https://github.com/yaml/pyyaml/issues/234
class Dumper(yaml.Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)


def main():
    args = docopt(__doc__, version='0.0.1')

    if args['init']:
        data = {
            "assets": {
                "Cash and Cash Equivalents": {
                    "Cash": ["Wallet"],
                    "Checking Accounts": ['Bank of America', 'Chase', 'Charles Schwab'],
                    "Savings Accounts": ['Bank of America (Cash Reserve)'],
                    "Other": ['Paypal', 'Venmo']
                },
                "Taxable Accounts": {
                    "Brokerage Accounts": ['Robinhood', 'Coinbase'],
                    "Online Funds": ['Fundrise', 'Lending Club']
                },
                "Tax-Advantaged Accounts (Retirement Accounts)": {
                    "401(k)s": ['Vanguard'],
                    "IRAs": ['Fidelity (Roth IRA)']
                },
                "Property": {
                    "Real Estate": ['Primary Residence', 'Investment Property'],
                    "Jewlery, Watches and Luxury Goods": ['Tag Heuer Watch', 'Gold Chain'],
                    "Vehicles": ['Primary Car', 'Recreational Car']
                },
                "Other Assets": {
                    "Life Insurance": ['MassMutual Cash Value'],
                    "Monies Owed": ['Parents', 'Friend']
                }
            },
            "liabilities": {
                "Short-Term Credit": {
                    "Short-Term Credit": ['Credit Card 1', 'Credit Card 2'],
                    "Loans and Mortgages": ['Primary Residence', 'Investment Property', 'Student Loan 1', 'Student Loan 2'],
                    "Other Liabilities": ['Other 1', 'Other 2']
                },
                "Loans and Mortgages": {
                    "Real Estate": ['Primary Residence', 'Investment Property'],
                    "Student Loans": ['Student Loan 1', 'Student Loan 2'],
                    "Auto Loans": ['Primary Car', 'Recreational Car']
                }
            }
        }

        def write_file():
            with open(args['--filepath'], 'w') as openfile:
                openfile.write(yaml.dump(data, sort_keys=False, Dumper=Dumper))

        if os.path.isfile(args['--filepath']):
            if args['--overwrite']:
                write_file()
            else:
                print(
                    "File already exists in this location, use '--overwrite' to continue anyways")
        else:
            write_file()

    elif args['run']:
        # Build/Check date
        if args['--date'] == 'today':
            args['--date'] = datetime.now().strftime('%Y-%m-%d')
        else:
            try:
                datetime.strptime(args['--date'], "%Y-%m-%d")
            except:
                print(
                    "\n'{}' does not match format 'YYYY-MM-DD'\n".format(args['--date']))

        app.main()
