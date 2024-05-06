# tests.py

from student import reverse_from_left, reverse_from_right

def test_reverse_functions():
    assert reverse_from_left("abcd") == "dcba", "Left to Right Reversal failed for 'abcd'"
    assert reverse_from_left("hello") == "olleh", "Left to Right Reversal failed for 'hello'"
    assert reverse_from_left("") == "", "Left to Right Reversal failed for empty string"
    assert reverse_from_left("a") == "a", "Left to Right Reversal failed for single character"

    assert reverse_from_right("abcd") == "dcba", "Right to Left Reversal failed for 'abcd'"
    assert reverse_from_right("hello") == "olleh", "Right to Left Reversal failed for 'hello'"
    assert reverse_from_right("") == "", "Right to Left Reversal failed for empty string"
    assert reverse_from_right("a") == "a", "Right to Left Reversal failed for single character"

def test_reverse_consistency():
    test_strings = ["example", "racecar", "12345", "teststring"]
    for string in test_strings:
        assert reverse_from_left(string) == reverse_from_right(string), f"Inconsistent results for {string}"
