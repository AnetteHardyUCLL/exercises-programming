import re


# using raw strings
def twice_repeated(string):
    return re.fullmatch(r"(.+)\1", string)


# # using escape sequences
# def twice_repeated(string):
#     return re.fullmatch("(.+)\\1", string)
