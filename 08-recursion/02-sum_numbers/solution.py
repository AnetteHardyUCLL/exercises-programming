def sum_numbers(number):
    # Convert number to absolute value to handle negative inputs as well
    number = abs(number)

    # Base case: if the number is a single digit
    if number < 10:
        return number

    # Recursive case: sum the last digit with the sum of the rest
    return (number % 10) + sum_numbers(number // 10)
