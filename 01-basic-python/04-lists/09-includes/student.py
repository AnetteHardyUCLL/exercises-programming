# Write your code here


def includes(xs, ys):
    for i in ys:
        if i not in xs:
            return False
    return True
