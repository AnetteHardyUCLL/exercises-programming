import pytest
from student import Money


@pytest.mark.parametrize("amount1", [0, 10, 25])
@pytest.mark.parametrize("amount2", [0, 50, 30])
@pytest.mark.parametrize("currency", ["EUR", "USD"])
def test_addition_same_currency(amount1, amount2, currency):
    money1 = Money(amount1, currency)
    money2 = Money(amount2, currency)
    money_total = money1 + money2
    assert money1.amount == amount1
    assert money2.amount == amount2
    assert money_total.amount == amount1 + amount2
    assert money_total.currency == currency


@pytest.mark.parametrize("amount1", [0, 10, 25])
@pytest.mark.parametrize("amount2", [0, 50, 30])
@pytest.mark.parametrize("currency1", ["EUR", "USD"])
@pytest.mark.parametrize("currency2", ["GBP", "JPY"])
def test_addition_different_currency(amount1, amount2, currency1, currency2):
    money1 = Money(amount1, currency1)
    money2 = Money(amount2, currency2)
    with pytest.raises(RuntimeError):
        money1 + money2


@pytest.mark.parametrize("amount1", [0, 10, 25])
@pytest.mark.parametrize("amount2", [0, 50, 30])
@pytest.mark.parametrize("currency", ["EUR", "USD"])
def test_subtraction_same_currency(amount1, amount2, currency):
    money1 = Money(amount1, currency)
    money2 = Money(amount2, currency)
    money_total = money1 - money2
    assert money1.amount == amount1
    assert money2.amount == amount2
    assert money_total.amount == amount1 - amount2
    assert money_total.currency == currency


@pytest.mark.parametrize("amount1", [0, 10, 25])
@pytest.mark.parametrize("amount2", [0, 50, 30])
@pytest.mark.parametrize("currency1", ["EUR", "USD"])
@pytest.mark.parametrize("currency2", ["GBP", "JPY"])
def test_subtraction_different_currency(amount1, amount2, currency1, currency2):
    money1 = Money(amount1, currency1)
    money2 = Money(amount2, currency2)
    with pytest.raises(RuntimeError):
        money1 - money2


@pytest.mark.parametrize("amount", [0, 10, 25])
@pytest.mark.parametrize("factor", [1, 2, 3 ])
@pytest.mark.parametrize("currency", ["EUR", "USD"])
def test_multiplication(amount, factor, currency):
    money = Money(amount, currency)
    money_multiplied = money * factor
    assert money_multiplied.amount == amount * factor
    assert money_multiplied.currency == currency
