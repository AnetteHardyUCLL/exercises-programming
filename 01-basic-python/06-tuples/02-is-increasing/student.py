# Write your code here


def is_increasing(ns):
    for x, y in zip(ns, ns[1:]):
        if x > y:
            return False
    return True
