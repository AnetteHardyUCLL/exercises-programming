import re


def remove_trailing_whitespace(string):
    return re.sub(r"\s+$", "", string, flags=re.MULTILINE)
