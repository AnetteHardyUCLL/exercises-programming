import re


def collect_links(string):
    return re.findall(r'<a href="(.*)">', string)


# The result depends on the number of capturing groups in the pattern
# If there are no groups, return a list of strings matching the whole pattern
# If there is exactly one group, return a list of strings matching that group
# If multiple groups are present, return a list of tuples of strings matching the groups
# Non-capturing groups do not affect the form of the result
