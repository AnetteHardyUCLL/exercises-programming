def findMaximum(lst):
    # Base case: if the list has only one item, return that item
    if len(lst) == 1:
        return lst[0]

    # Recursive case: compare the first element to the maximum of the rest of the list
    else:
        max_of_rest = findMaximum(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest
