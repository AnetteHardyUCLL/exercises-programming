def matching_parentheses(string):
    count = 0
    for char in string:
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0
