import pytest
import student
import solution
from copy import copy


@pytest.mark.parametrize("xs, n", [
    ([1], 0),
    ([1, 2], 0),
    ([1, 2], 1),
    ([1, 2, 3], 0),
    ([1, 2, 3], 1),
    ([1, 2, 3], 2),
    ([1, 2, 3], 3),
    (['a', 'b', 'c', 'd', 'e'], 0),
    (['a', 'b', 'c', 'd', 'e'], 1),
    (['a', 'b', 'c', 'd', 'e'], 2),
    (['a', 'b', 'c', 'd', 'e'], 3),
    (['a', 'b', 'c', 'd', 'e'], 4),
])
def test_function(xs, n):
    function_name = 'rotate'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual_xs = copy(xs)
    a = student_function(actual_xs, n)
    expected_xs = copy(xs)
    b = solution_function(expected_xs, n)

    assert a == b, f"Wrong result for {(xs, n)}, expected {a}, received {b}"
