def indices_of(xs, condition):
    return [i for i in range(len(xs)) if condition(xs[i])]
