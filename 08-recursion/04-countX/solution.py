def countX(text):
    # Base case: If the text is empty, return 0
    if not text:
        return 0

    # Check if the first character is 'x'
    first_is_x = 1 if text[0] == 'x' else 0

    # Recursive call on the rest of the text
    return first_is_x + countX(text[1:])
