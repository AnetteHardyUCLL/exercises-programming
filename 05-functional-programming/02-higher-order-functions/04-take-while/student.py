def take_while(xs, condition):
    i = 0
    while i < len(xs) and condition(xs[i]):
        i += 1
    return (xs[:i], xs[i:])
