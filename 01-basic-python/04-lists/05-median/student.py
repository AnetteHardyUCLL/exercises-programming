# Write your code here


def median(ns):
    ns.sort()
    middle_value = len(ns) // 2
    if len(ns) % 2 != 0:
        return ns[middle_value]
    else:
        return (ns[middle_value] + ns[(middle_value - 1)]) / 2
