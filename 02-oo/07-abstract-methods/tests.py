import inspect
import pytest
from student import *


def is_class_abstract(c):
    return inspect.isabstract(c)


def test_a_is_abstract():
    assert is_class_abstract(A)


def test_b_is_not_abstract():
    assert not is_class_abstract(B)


def test_c_is_not_abstract():
    assert not is_class_abstract(C)


def test_d_is_abstract():
    assert is_class_abstract(D)


def test_e_is_not_abstract():
    assert not is_class_abstract(E)


def test_f_is_not_abstract():
    assert is_class_abstract(F)


@pytest.mark.parametrize('method, presence', [
    ('a', True),
    ('b', True),
    ('c', True),
    ('d', False),
    ('e', True),
    ('f', False),
    ('g', False),
])
def test_A_methods(method, presence):
    assert hasattr(A, method) == presence


@pytest.mark.parametrize('method, presence', [
    ('a', True),
    ('b', True),
    ('c', True),
    ('d', False),
    ('e', True),
    ('f', False),
    ('g', False),
])
def test_B_methods(method, presence):
    assert hasattr(B, method) == presence


@pytest.mark.parametrize('method, presence', [
    ('a', True),
    ('b', True),
    ('c', True),
    ('d', False),
    ('e', True),
    ('f', True),
    ('g', False),
])
def test_C_methods(method, presence):
    assert hasattr(C, method) == presence


@pytest.mark.parametrize('method, presence', [
    ('a', True),
    ('b', True),
    ('c', True),
    ('d', False),
    ('e', True),
    ('f', True),
    ('g', False),
])
def test_D_methods(method, presence):
    assert hasattr(D, method) == presence


@pytest.mark.parametrize('method, presence', [
    ('a', True),
    ('b', True),
    ('c', True),
    ('d', False),
    ('e', True),
    ('f', True),
    ('g', True),
])
def test_E_methods(method, presence):
    assert hasattr(E, method) == presence


@pytest.mark.parametrize('method, presence', [
    ('a', True),
    ('b', True),
    ('c', False),
    ('d', False),
    ('e', False),
    ('f', True),
    ('g', False),
])
def test_F_methods(method, presence):
    assert hasattr(F, method) == presence
