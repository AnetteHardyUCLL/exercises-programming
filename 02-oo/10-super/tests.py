import pytest
from inspect import isabstract
from pytest import approx
from math import pi
from student import *


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in globals(), reason=f'{class_name} is not defined')


@if_class_exists('Rectangle')
@pytest.mark.parametrize('width, length, expected_perimeter', [
    (1, 1, 4),
    (1, 2, 6),
    (2, 4, 12),
])
def test_rectangle_perimeter(width, length, expected_perimeter):
    rectangle = Rectangle(width=width, length=length)
    assert expected_perimeter == rectangle.perimeter


@if_class_exists('Rectangle')
@pytest.mark.parametrize('width, length, expected_area', [
    (1, 1, 1),
    (1, 2, 2),
    (2, 4, 8),
])
def test_rectangle_area(width, length, expected_area):
    rectangle = Rectangle(width=width, length=length)
    assert expected_area == rectangle.area


@if_class_exists('Rectangle')
@pytest.mark.parametrize('property_name', [
    'width',
    'length',
    'perimeter',
    'area',
])
def test_rectangle_properties_are_readonly(property_name):
    rectangle = Rectangle(width=1, length=2)
    assert hasattr(rectangle, property_name)
    with pytest.raises(AttributeError):
        setattr(rectangle, property_name, 2)


@if_class_exists('Rectangle')
def test_rectangle_is_shape():
    assert Shape in Rectangle.__mro__


@if_class_exists('Square')
@pytest.mark.parametrize('side, expected_perimeter', [
    (1, 4),
    (2, 8),
    (3, 12),
])
def test_square_perimeter(side, expected_perimeter):
    square = Square(side=side)
    assert expected_perimeter == square.perimeter


@if_class_exists('Square')
@pytest.mark.parametrize('side, expected_area', [
    (1, 1),
    (2, 4),
    (3, 9),
])
def test_square_area(side, expected_area):
    square = Square(side=side)
    assert expected_area == square.area


@if_class_exists('Square')
@pytest.mark.parametrize('property_name', [
    'width',
    'length',
    'side',
    'perimeter',
    'area',
])
def test_square_properties_are_readonly(property_name):
    square = Square(side=1)
    assert hasattr(square, property_name)
    with pytest.raises(AttributeError):
        setattr(square, property_name, 2)


@if_class_exists('Square')
def test_square_is_rectangle():
    assert Rectangle in Square.__mro__


@if_class_exists('Ellipse')
@pytest.mark.parametrize('r1, r2, expected_area', [
    (2, 1, pi * 2 * 1),
    (3, 2, pi * 3 * 2),
    (4, 1, pi * 4 * 1),
])
def test_ellipse_area(r1, r2, expected_area):
    ellipse = Ellipse(major_radius=r1, minor_radius=r2)
    assert expected_area == ellipse.area


@if_class_exists('Ellipse')
def test_ellipse_has_no_perimeter():
    ellipse = Ellipse(major_radius=2, minor_radius=1)
    with pytest.raises(NotImplementedError):
        ellipse.perimeter



@if_class_exists('Ellipse')
@pytest.mark.parametrize('property_name', [
    'minor_radius',
    'major_radius',
    'area',
])
def test_ellipse_properties_are_readonly(property_name):
    ellipse = Ellipse(major_radius=2, minor_radius=1)
    assert hasattr(ellipse, property_name)
    with pytest.raises(AttributeError):
        setattr(ellipse, property_name, 2)


@if_class_exists('Ellipse')
def test_ellipse_is_shape():
    assert Shape in Ellipse.__mro__


@if_class_exists('Circle')
@pytest.mark.parametrize('radius, expected_perimeter', [
    (1, 2 * pi * 1),
    (2, 2 * pi * 2),
    (3, 2 * pi * 3),
])
def test_circle_perimeter(radius, expected_perimeter):
    circle = Circle(radius=radius)
    assert approx(expected_perimeter) == circle.perimeter


@if_class_exists('Circle')
@pytest.mark.parametrize('radius, expected_area', [
    (1, pi * 1**2),
    (2, pi * 2**2),
    (3, pi * 3**2),
])
def test_circle_area(radius, expected_area):
    circle = Circle(radius=radius)
    assert approx(expected_area) == circle.area


@if_class_exists('Circle')
@pytest.mark.parametrize('property_name', [
    'minor_radius',
    'major_radius',
    'radius',
    'perimeter',
    'area',
])
def test_circle_properties_are_readonly(property_name):
    circle = Circle(radius=1)
    assert hasattr(circle, property_name)
    with pytest.raises(AttributeError):
        setattr(circle, property_name, 2)


@if_class_exists('Circle')
def test_circle_is_ellipse():
    assert Ellipse in Circle.__mro__


@if_class_exists('Rectangle')
def test_rectangle_is_not_abstract():
    assert not isabstract(Rectangle)


@if_class_exists('Square')
def test_square_is_not_abstract():
    assert not isabstract(Square)


@if_class_exists('Ellipse')
def test_ellipse_is_not_abstract():
    assert not isabstract(Ellipse)


@if_class_exists('Circle')
def test_circle_is_not_abstract():
    assert not isabstract(Circle)
