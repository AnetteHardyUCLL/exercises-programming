import re


def is_valid_password(string):
    positive_regexes = [
        r".{12,}",
        r"[0-9]",
        r"[a-z]",
        r"[A-Z]",
        r"[-+/.*@]",
    ]

    negative_regexes = [r"(.)\1{2}", r"(.)(.*\1){3}"]

    for regex in positive_regexes:
        if not re.search(regex, string):
            return False

    for regex in negative_regexes:
        if re.search(regex, string):
            return False

    return True
