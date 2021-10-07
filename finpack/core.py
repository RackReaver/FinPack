"""FinPack
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

import csv
from datetime import datetime

from finpack import utils

class DataError(Exception):
    pass

class Account():
    def __init__(self, name, type, category, sub_category, description, history):
        self.name = name
        self.short_name = name[:40]
        self.type = type
        self.category = category
        self.sub_category = sub_category
        self.description = description
        self.history = history
        
        if len(self.name) > 40:
            self.short_name = name[:37] + '...'

    def __repr__(self):
        return '<Account.' + self.type + '.' + self.name.replace(' ', '-') + '>'

    def __eq__(self, other):
        return ' '.join([self.type, self.name]) == other

    def current_value(self):
        """Get latest monetary value of account.
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


def importer(filepath, header=True):
    """Import chart of accounts from CSV file.
    
    args:
        filepath (str): Location of CSV file.
    kwargs:
        header (bool): If column names are included in file.

    return (dict): 
    """
    accounts = []

    with open(filepath, 'r') as openFile:
        r = csv.DictReader(openFile)
        # Loop through all rows
        for row in r:

            # Check if account name already exists
            if ' '.join([row['type'], row['name']]) in accounts:
                raise DataError('Account names must be unique')

            ignore = ['name', 'type', 'category', 'sub_category', 'description']
            # Parse out only financial data
            data = [[x[0], x[1].replace(',', '')] for x in row.items() if x[0] not in ignore]

            # Add account to accounts list
            accounts.append(Account(
                                name=row['name'],
                                type=row['type'],
                                category=row['category'],
                                sub_category=row['sub_category'],
                                description=row['description'],
                                history=data
                                ))

    return accounts