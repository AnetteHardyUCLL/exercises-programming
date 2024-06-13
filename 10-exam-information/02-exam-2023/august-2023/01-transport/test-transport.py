import pytest
from transport import *


@pytest.mark.parametrize(
    "amount_of_seats",
    [1, 2, 3, 4],
)
def test_maximum_occupants_taxi(amount_of_seats):
    taxi = Taxi("1-NGL-760", amount_of_seats)
    max_occupants = amount_of_seats

    assert taxi.maximum_occupants == max_occupants


@pytest.mark.parametrize(
    "amount_of_seats",
    [10, 20, 30, 35],
)
def test_maximum_occupants_bus(amount_of_seats):
    bus = Bus("1-HUE-344", amount_of_seats)
    max_occupants = 2 * amount_of_seats

    assert bus.maximum_occupants == max_occupants
