import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize(
    "string",
    [
        "",
        "()",
        "(())",
        "()()()",
        "(())()",
    ],
)
def test_matching_parenthesis(string):
    assert matching_parentheses(string), f"{string} has matching parentheses"


@pytest.mark.parametrize(
    "string",
    [
        "(",
        ")",
        ")(",
        "(()))(()",
    ],
)
def test_matching_parenthesis(string):
    assert not matching_parentheses(string), f"{string} has unmatched parentheses"
