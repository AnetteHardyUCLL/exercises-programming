# Write your code here


def add_indices(xs):
    indices = range(len(xs))
    return list(zip(indices, xs))


def add_indices(xs):
    return list(enumerate(xs))
