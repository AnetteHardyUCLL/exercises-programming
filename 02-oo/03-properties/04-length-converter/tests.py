import pytest
from pytest import approx
from student import *


@pytest.mark.parametrize('meter, feet', [
    (0, 0),
    (1, 3.28),
    (5, 16.4),
    (10, 32.8),
])
def test_meter_to_feet(meter, feet):
    converter = LengthConverter()
    converter.meter = meter
    assert converter.feet == approx(feet, rel=0.01)

    converter.feet = feet
    assert converter.meter == approx(meter, rel=0.01)


@pytest.mark.parametrize('meter, inch', [
    (0, 0),
    (1, 39.4),
    (5, 196.8),
    (10, 393.7),
])
def test_meter_to_inch(meter, inch):
    converter = LengthConverter()
    converter.meter = meter
    assert converter.inch == approx(inch, rel=0.01)

    converter.inch = inch
    assert converter.meter == approx(meter, rel=0.01)


@pytest.mark.parametrize('feet, inch', [
    (0, 0),
    (1, 12),
    (5, 60),
    (10, 120),
])
def test_feet_to_inch(feet, inch):
    converter = LengthConverter()
    converter.feet = feet
    assert converter.inch == approx(inch, rel=0.01)

    converter.inch = inch
    assert converter.feet == approx(feet, rel=0.01)
