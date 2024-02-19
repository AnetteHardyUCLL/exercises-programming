import pytest
from pytest import approx
from student import *


@pytest.mark.parametrize('weight,height,expected_bmi,expected_category', [
    (50, 1.80, approx(15.4, abs=0.1), 'underweight'),
    (70, 1.70, approx(24.2, abs=0.1), 'normal'),
    (150, 1.90, approx(41.5, abs=0.1), 'overweight'),
])
def test_calculator(weight, height, expected_bmi, expected_category):
    calc = BMICalculator(weight_in_kg=weight, height_in_m=height)
    assert calc.bmi == expected_bmi
    assert calc.category == expected_category
