# Write your code here


# def rotate(xs, n):
#     for _ in range(n):
#         x = xs.pop(0)
#         xs.append(x)
#     return xs


def rotate(xs, n):
    xs[:] = xs[n:] + xs[:n]
    return xs
