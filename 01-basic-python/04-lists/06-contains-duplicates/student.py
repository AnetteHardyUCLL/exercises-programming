# Write your code here


def contains_duplicates(xs):
    sorted_list = sorted(xs)
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] == sorted_list[i + 1]:
            return True
    return False
