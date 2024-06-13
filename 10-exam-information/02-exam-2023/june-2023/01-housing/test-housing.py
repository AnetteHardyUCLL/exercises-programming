import pytest
from housing import *


# WITH EXPECTED VALUES IN PARAMETRIZE
# helper function for expected value
def maximum_occupants_villa(area, number_of_rooms):
    return min(area // 20, number_of_rooms * 2)


@pytest.mark.parametrize(
    "area, number_of_rooms, expected",
    [
        (151, 4, maximum_occupants_villa(151, 4)),
        (90, 2, maximum_occupants_villa(90, 2)),
        (100, 3, maximum_occupants_villa(100, 3)),
        (200, 5, maximum_occupants_villa(200, 5)),
    ],
)
def test_maximum_occupants_villa(area, number_of_rooms, expected):
    # create villa
    villa = Villa("Roeselbergdal 44, 3012 Wilsele", area, number_of_rooms, 1)

    assert villa.maximum_occupants == expected


@pytest.mark.parametrize(
    "area",
    [151, 90, 100, 200],
)
@pytest.mark.parametrize(
    "number_of_rooms",
    [4, 2, 3, 5],
)
def test_maximum_occupants_villa(area, number_of_rooms):
    # create villa
    villa = Villa("Roeselbergdal 44, 3012 Wilsele", area, number_of_rooms, 1)

    # maximum_occupants formula
    maximum_occupants = min(area // 20, number_of_rooms * 2)

    assert villa.maximum_occupants == maximum_occupants


@pytest.mark.parametrize(
    "area",
    [20, 30, 40, 72],
)
def test_maximum_occupants_kot(area):
    # create kot
    kot = StudentKot("Kortestraat 6, 3000 Leuven", area)

    # maximum_occupants formula
    maximum_occupants = min(area // 20, 2)

    assert kot.maximum_occupants == maximum_occupants
