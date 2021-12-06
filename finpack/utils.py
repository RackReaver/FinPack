"""Code used accross the code base but not directly related to any single file.
"""
__copyright__ = "Copyright (C) 2021 Matt Ferreira"


def _add_char(num, char=" "):
    """Creates a string value give a number and character.
    args:
        num (int): Amount to repeat character
    kwargs:
        char (str): Character value to loop
    Returns (str): Iterated string value for given character
    """
    string = ""
    for i in range(num):
        string += char
    return string
