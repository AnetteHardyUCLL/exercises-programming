import re


def only_digits(string):
    return re.fullmatch("[0-9]*", string)
