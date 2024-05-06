def group_by(xs, key_function):
    dictionary = {}
    for x in xs:
        key = key_function(x)
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(x)
    return dictionary
