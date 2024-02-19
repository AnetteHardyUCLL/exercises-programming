import pytest
from student import *


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in globals(), reason=f'{class_name} is not defined')


@if_class_exists('Item')
@pytest.mark.parametrize('age', [17, 18, 19])
@pytest.mark.parametrize('country', ['Belgium', 'Arstotzka'])
def test_regular_item(age, country):
    customer = Customer('Chris', age, country)
    item = Item('banana', 10)
    assert item.can_be_sold_to(customer)


@if_class_exists('AgeRestrictedItem')
@pytest.mark.parametrize('age, expected', [
    *((age, False) for age in range(0, 18)),
    *((age, True) for age in range(18, 30)),
])
@pytest.mark.parametrize('country', ['Belgium', 'Arstotzka'])
def test_age_restricted_item(age, country, expected):
    customer = Customer("John", age, country)
    item = AgeRestrictedItem('tobacco', 15)
    assert item.can_be_sold_to(customer) == expected


@if_class_exists('AgeRestrictedItem')
@pytest.mark.parametrize('country, expected', [
    ('Belgium', True),
    ('France', True),
    ('Arstotzka', False),
])
@pytest.mark.parametrize('age', [17, 18, 19])
def test_country_restricted_item(age, country, expected):
    customer = Customer("Kim", age, country)
    item = CountryRestrictedItem('tobacco', 15)
    assert item.can_be_sold_to(customer) == expected
