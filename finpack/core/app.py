"""Interactive App
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

import os

from finpack.utils.table import create_table


def main():
    response = menu()
    while True:
        if response == '1' or response == '2' or response == '3':
            break
        response = menu()


def menu():
    """Menu for interactive app

    return (str): Input Prompt
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print(create_table([['1. Assets'],
                        ['2. Liabilities'],
                        ['3. Incomes'],
                        ['4. Expenses'],
                        ['5. Assets & Liabilites'],
                        ['6. Incomes & Expenses']],
                       headers=[['Interactive App']]))
    return input(' Selection: ')
