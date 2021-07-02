"""Exporter for Balance Sheet and Cashflow Statement.
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

import os


def balance_sheet_csv(assets: dict, liabilities: dict, date):

    FOLDER_NAME = 'balance_sheets'

    final_filename = os.path.join(
        FOLDER_NAME, '{} - Balance Sheet'.format(date)) + '.csv'

    # Get list length
    if len(assets) > len(liabilities):
        min_len = len(assets)
    else:
        min_len = len(liabilities)

    # Generate empty list
    rows = ['' for x in range(0, min_len+2)]

    total_assets = 0
    count = 0
    for category, sub_categories in assets.items():
        for sub_category, accounts in sub_categories.items():
            for account, value in accounts.items():
                total_assets += value
                rows[count] = '{},{},{},{:0.2f},'.format(category,
                                                         sub_category,
                                                         account,
                                                         value)
                count += 1

    total_liabilities = 0
    count = 0
    for category, sub_categories in liabilities.items():
        for sub_category, accounts in sub_categories.items():
            for account, value in accounts.items():
                total_liabilities += value
                rows[count] += '{},{},{},{:0.2f},'.format(category,
                                                          sub_category,
                                                          account,
                                                          value)
                count += 1

    rows.append(',,,,,,{},{}'.format(
        'TOTAL NET WORTH', round(total_assets-total_liabilities, 2)))

    # Creates sub-folder if one does not exist
    if os.path.isdir(FOLDER_NAME) is not True:
        # logging.info('subFolder not found... Creating now.')
        os.makedirs(FOLDER_NAME)

    with open(final_filename, 'w') as openFile:
        openFile.write('Balance Sheet as of {}'.format(date))
        openFile.write('\n\nAssets,,,,Liabilities,,,\n')
        openFile.write(
            'Category,Sub-Category,Account,Value,Category,Sub-Category,Account,Value\n')
        for row in rows:
            openFile.write(row + '\n')
