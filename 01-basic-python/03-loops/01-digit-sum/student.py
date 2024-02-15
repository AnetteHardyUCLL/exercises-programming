# Write your code here
from math import floor


def last_digit(n):
    return n % 10


def remove_last_digit(n):
    return n // 10


def digit_sum(n):
    sum = 0
    while n > 0:
        sum += last_digit(n)
        n = remove_last_digit(n)
    return sum
