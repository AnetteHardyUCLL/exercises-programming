# tests.py

from student import sum_numbers

def test_sum_numbers_simple():
    assert sum_numbers(234) == 9, "Sum of 234 should be 9"
    assert sum_numbers(1001) == 2, "Sum of 1001 should be 2"
    assert sum_numbers(0) == 0, "Sum of 0 should be 0"

def test_sum_numbers_negative():
    assert sum_numbers(-234) == 9, "Sum of -234 should be 9"
    assert sum_numbers(-1001) == 2, "Sum of -1001 should be 2"

def test_sum_numbers_large():
    assert sum_numbers(123456789) == 45, "Sum of 123456789 should be 45"
