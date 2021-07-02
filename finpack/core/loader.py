""" 
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

import yaml


def loader(filepath: str, imports=['assets', 'liabilities', 'incomes', 'expenses']):
    """Import YAML data.

    args:
        filepath (str): Filepath of *.yaml file

    kwargs:
        imports (list): List root_types to look for and import.

    return: {"assets": {}, "liabilities": {}, "incomes": {}, "expenses": {}}
    """

    with open(filepath, 'r') as openFile:
        accounts = yaml.safe_load(openFile)

    data = {}

    if 'assets' in accounts and 'assets' in imports:
        data['assets'] = _importer('assets', accounts)
    if 'liabilities' in accounts and 'liabilities' in imports:
        data['liabilities'] = _importer('liabilities', accounts)
    if 'incomes' in accounts and 'incomes' in imports:
        data['incomes'] = _importer('incomes', accounts)
    if 'expenses' in accounts and 'expenses' in imports:
        data['expenses'] = _importer('expenses', accounts)

    return data


def _importer(root_type: str, accounts: dict):
    """
    """
    cat_dict = {}
    for category, sub_categories in accounts[root_type].items():
        cat_dict[category] = {}

        if sub_categories != None:
            for sub_category, accounts in sub_categories.items():
                cat_dict[category][sub_category] = {}

                if accounts != None:
                    for account in accounts:
                        cat_dict[category][sub_category][account] = 0

    return cat_dict
