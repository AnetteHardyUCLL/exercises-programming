import pytest
from student import *
from inspect import isabstract


def test_shape_exists():
    assert 'Shape' in globals()


@pytest.mark.parametrize('the_class', [Rectangle, Circle])
def test_is_child_of_shape(the_class):
    assert Shape in the_class.__mro__


def test_shape_is_abstract():
    assert isabstract(Shape)


@pytest.mark.parametrize('property_name', [
    'perimeter',
    'area'
])
def test_shape_contains_area_property(property_name):
    assert hasattr(Shape, property_name)
