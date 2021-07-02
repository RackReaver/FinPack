"""Interactive App
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

import os
import sys

from finpack.core.loader import loader
from finpack.core.exporter import balance_sheet_csv
from finpack.utils.table import create_table


def main(cli):
    """Interactive app for generating financial data.
    """
    response = main_menu()
    while True:
        response = response.strip()
        if response in ['1', '2', '3', '4', '5', '6', '7', '', ' ']:
            break
        response = main_menu()

    # Run loader for selected response
    if response == '1':
        data = loader(cli['--filepath'], imports=['assets', 'liabilities'])
    elif response == '2':
        data = loader(cli['--filepath'], imports=['incomes', 'expenses'])
    else:
        data = loader(cli['--filepath'])

    # Run Interactive Updater
    export_data = interactive_updater(data)

    balance_sheet_csv(export_data['assets'],
                      export_data['liabilities'], cli['--date'])


def main_menu():
    """Main menu for app.

    return (str): Input Prompt
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print(create_table([['1. Assets & Liabilites'],
                        ['2. Incomes & Expenses'],
                        ['3. All']],
                       headers=[['Interactive App']]))
    return input(' Run (3): ')


def interactive_updater(data):

    # Get total accounts
    total_accounts = _get_total_accounts(data)

    count = 1
    for root_type, categories in data.items():
        for category, sub_categories in categories.items():
            for sub_category, accounts in sub_categories.items():
                for account, value in accounts.items():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    str_export = ''
                    str_export += '\n+-------------------------+\t+-------------------------------+'
                    str_export += '\n| {}{} of {}{} Total Accounts |\t'.format(
                        count, _get_padding(str(count), 2), _get_padding(str(total_accounts), 2), total_accounts)
                    str_export += '| "s" to skip account\t\t|'
                    str_export += '\n+-------------------------+\t+-------------------------------+'
                    str_export += '\n| {}\t\t  |\t'.format(root_type)
                    str_export += '| "e" to exit app forcefully\t|'
                    str_export += '\n+-------------------------+\t+-------------------------------+'
                    str_export += '\n\n{} -> {} -> {}'.format(
                        category, sub_category, account)
                    print(str_export)

                    # Extract value and add to data dictionary
                    value = input('\nCurrent Value: ')
                    if value == 'e':
                        print('Quit without saving...')
                        sys.exit()
                    elif value == 's':
                        pass
                    else:
                        while True:
                            value = value.replace(',', '').strip()

                            try:
                                float(value)
                                break
                            except:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print(str_export)
                                print('\nPlease enter a valid number...')
                                value = input('Current Value: ')

                        data[root_type][category][sub_category][account] = float(
                            value)

                    count += 1

    return data


def _get_total_accounts(data: dict):
    total_accounts = 0
    for categories in data.values():
        for sub_categories in categories.values():
            for accounts in sub_categories.values():
                for account in accounts:
                    total_accounts += 1

    return total_accounts


def _get_padding(var: str, max_value: int):
    if len(var) == max_value:
        return ''
    else:
        string = ''
        for i in range(max_value - len(var)):
            string += ' '

        return string
