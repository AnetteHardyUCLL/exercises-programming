def find(list, condition):
    for value in list:
        if condition(value):
            return value
    return None
