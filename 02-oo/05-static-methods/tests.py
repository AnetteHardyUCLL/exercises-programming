import pytest
from student import *


@pytest.mark.parametrize('init_amount, init_unit, conversion_amount, conversion_unit', [
    (1, 'seconds', 1, 'seconds'),
    (1, 'minutes', 60, 'seconds'),
    (1, 'hours', 3600, 'seconds'),
    (2, 'seconds', 2, 'seconds'),
    (2, 'minutes', 2 * 60, 'seconds'),
    (5, 'minutes', 5 * 60, 'seconds'),
    (60, 'minutes', 1, 'hours'),
    (5 * 60, 'minutes', 5, 'hours'),
])
def test_from_seconds(init_amount, init_unit, conversion_amount, conversion_unit):
    factory_name = f'from_{init_unit}'
    property_name = conversion_unit

    if not hasattr(Duration, factory_name):
        pytest.skip(f'Factory {factory_name} not implemented')
    if not hasattr(Duration, property_name):
        pytest.skip(f'Property {property_name} not implemented')

    duration = getattr(Duration, factory_name)(init_amount)
    actual = getattr(duration, property_name)

    assert actual == conversion_amount

