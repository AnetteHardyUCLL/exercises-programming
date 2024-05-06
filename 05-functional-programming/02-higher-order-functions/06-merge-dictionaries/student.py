def merge_dictionaries(d1, d2, merge_function):
    for d1_key in d1:
        if d1_key in d2:
            new_value = merge_function(d1[d1_key], d2[d1_key])
            d2[d1_key] = new_value
    return {**d1, **d2}
