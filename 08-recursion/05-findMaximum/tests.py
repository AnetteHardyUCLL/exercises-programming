# tests.py

from student import findMaximum
import pytest

def test_findMaximum():
    assert findMaximum([1, 2, 3, 4, 5]) == 5, "The maximum of [1, 2, 3, 4, 5] should be 5"
    assert findMaximum([5, 4, 3, 2, 1]) == 5, "The maximum of [5, 4, 3, 2, 1] should be 5"
    assert findMaximum([2, 3, 1, 6, 4]) == 6, "The maximum of [2, 3, 1, 6, 4] should be 6"
    assert findMaximum([-10, -3, -20, -5]) == -3, "The maximum of negative numbers should be the least negative"
    assert findMaximum([100]) == 100, "The maximum of single element list should be the element itself"
    assert findMaximum([1, 100, 50, 100]) == 100, "The maximum where duplicate maximum exists should still be correct"

# Adding a test for an empty list
def test_findMaximum_empty():
    with pytest.raises(IndexError):
        findMaximum([])  # Expect an error when the list is empty
