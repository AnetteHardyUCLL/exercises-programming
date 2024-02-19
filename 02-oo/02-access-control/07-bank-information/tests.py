from student import BankAccount
import pytest

def test_bank_account_initialization():
    account = BankAccount("123456", 1000)
    assert account.get_account_number() == "123456"
    assert account.get_balance() == 1000

def test_bank_account_deposit():
    account = BankAccount("123456", 1000)
    account.deposit(500)
    assert account.get_balance() == 1500

def test_bank_account_deposit_negative_amount():
    account = BankAccount("123456", 1000)
    with pytest.raises(ValueError):
        account.deposit(-500)

def test_bank_account_withdraw():
    account = BankAccount("123456", 1000)
    account.withdraw(500)
    assert account.get_balance() == 500

def test_bank_account_withdraw_negative_amount():
    account = BankAccount("123456", 1000)
    with pytest.raises(ValueError):
        account.withdraw(-500)

def test_bank_account_insufficient_funds():
    account = BankAccount("123456", 1000)
    with pytest.raises(ValueError):
        account.withdraw(1500)

def test_bank_account_insufficient_funds_deposit():
    account = BankAccount("123456", 1000)
    with pytest.raises(ValueError):
        account.withdraw(5000)

# Run the tests
if __name__ == "__main__":
    pytest.main()
