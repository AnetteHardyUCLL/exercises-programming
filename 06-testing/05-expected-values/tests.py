import itertools
import pytest
from mergesort import merge_sort, merge_sorted, split_in_two


@pytest.mark.parametrize(
    "ns", [list(range(k)) for k in range(101)]
)  # generate a list of lists [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], ...]
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(left) - len(right)) <= 1


@pytest.mark.parametrize(
    "left",
    [
        [],
        [0, 1, 2, 3],
        [0, 2, 4, 6],
        [1, 3, 5, 7],
        [5, 5, 5],
        [3, 7, 7, 11, 15],
    ],
)
@pytest.mark.parametrize(
    "right",
    [
        [],
        [0, 1, 2, 3],
        [0, 2, 4, 6],
        [1, 3, 5, 7],
        [5, 5, 5],
        [3, 7, 7, 11, 15],
    ],
)
def test_merge_sorted(left, right):
    actual = merge_sorted(left, right)
    expected = sorted(left + right)
    assert expected == actual


@pytest.mark.parametrize(
    "expected, ns",
    [
        (ns, list(permutation))
        for ns in [[], [1], [1, 2], [1, 4, 4, 6], [1, 2, 2, 4, 6, 9]]
        for permutation in itertools.permutations(ns)
    ],
)
def test_merge_sort(expected, ns):
    assert merge_sort(ns) == expected
