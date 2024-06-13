def split_in_two(ns):
    return (ns[: len(ns) // 2], ns[len(ns) // 2 :])  # floor division to find the middle


def merge_sorted(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(
        left[i:]
    )  # we use extend because it is possible that there are still elements remaining in the list that weren't taken into account at the end of the while loop
    result.extend(right[j:])
    return result


def merge_sort(ns):
    if len(ns) <= 1:
        return ns
    left, right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge_sorted(sorted_left, sorted_right)
