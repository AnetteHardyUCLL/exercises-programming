# tests.py

from student import countX

def test_countX():
    assert countX("axbxcxd") == 3, "Should count three 'x' characters"
    assert countX("abcd") == 0, "Should count zero 'x' characters"
    assert countX("xxxxx") == 5, "Should count five 'x' characters"
    assert countX("") == 0, "Should count zero 'x' characters in an empty string"
    assert countX("x") == 1, "Should count one 'x' character"
    assert countX("XxXx") == 2, "Should count two 'x' characters (case-sensitive)"
