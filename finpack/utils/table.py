"""Table rendering.
"""
__copyright__ = "Copyright (C) 2020  Matt Ferreira"
__license__ = "Apache License"


def create_table(rows, headers=None):
    """Converts data to a table that can be sent stdout.
    args:
        rows (list): Equalized tuple of tuples
                        (i.e. [['data', 'value'], ['data2', 'value2']])
    kwargs:
        headers (list): Tuple of one or more headers for columns
                        (i.e. [['head1col1', 'head1col2'], ['head2col1', 'head2col2']])
    Return (str): Table string ready for stdout.
    """
    if headers != None:
        assert isinstance(headers, list)
    assert isinstance(rows, list)
    ROWS = rows
    COLUMN_SPACER = 1

    export_str = ''

    # Compute the required width for row columns
    first = True
    col_widths = get_col_widths(ROWS[0])
    for num, row in enumerate(ROWS):
        if num != 0:
            col_widths = get_col_widths(row, col_widths=col_widths)

    if headers != None:
        # Compute the required width for header columns
        for header in headers:
            col_widths = get_col_widths(header, col_widths=col_widths)

    # Add padding to each col
    col_widths = [x+COLUMN_SPACER for x in col_widths]
    col_widths = list(col_widths)

    line_break = '+' + \
        _add_char(sum(col_widths)+COLUMN_SPACER *
                  len(col_widths)*2, char='-') + '+'
    export_str += line_break + '\n'
    if headers != None:
        for header in headers:
            export_str += _create_row(header, COLUMN_SPACER, col_widths)
            export_str += line_break + '\n'

    for row in ROWS:
        export_str += _create_row(row, COLUMN_SPACER, col_widths)

    export_str += line_break
    return export_str


def _add_char(num, char=' '):
    """Creates a string value give a number and character.
    args:
        num (int): Amount to repeat character
    kwargs:
        char (str): Character value to lopp
    Returns (str): Iterated string value for given character
    """
    string = ''
    for i in range(num):
        string += char
    return string


def _create_row(row, padding, col_widths):
    """Creates a table row.
    args:
        row (list): Column values for row.
        padding (int): Number of spaces between columns
        col_widths (list): Width requirements for each column
    Return (str): Row value in string format.
    """
    export_str = ''
    for num, col in enumerate(row):
        col_width = 0
        # Compute difference in width for each column item
        if len(str(col)) < col_widths[num]:
            col_width = col_widths[num] - len(str(col))

        string = '|{}{}'.format(_add_char(padding), col)
        string += _add_char(col_width)
        if num+1 == len(col_widths):
            string += '{}|\n'.format(_add_char(padding))

        # Add string computation to main str
        export_str += string

    return export_str


def get_col_widths(columns, col_widths=None):
    """Get the max required width for a set of columns.
    args:
        columns (list): A list of strings.
    kwargs:
        col_widths (list): Allow import of existing list of col_widths.
    Return (list): Computed max column widths.
    """
    assert isinstance(columns, list)
    if col_widths != None:
        assert isinstance(col_widths, list)
        col_widths = col_widths
        assert len(columns) == len(col_widths), "Lists do not match in length. {} != {}".format(
            len(columns), len(col_widths))
    else:
        col_widths = [0 for x in range(len(columns))]

    for num, row in enumerate(columns):
        if len(str(row)) > col_widths[num]:
            col_widths[num] = len(str(row))

    return col_widths
