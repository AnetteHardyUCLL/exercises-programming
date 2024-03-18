import re


def remove_repeated_words(string):
    return re.sub(r"(\b[a-zA-Z]+\b)( \1)+", r"\1", string)
