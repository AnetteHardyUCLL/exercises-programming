import pytest
from student import *


def test_account():
    password = 'FPak18@PQL91+'
    account = Account('r0077643', password)
    assert account.is_correct_password(password)
    assert not account.is_correct_password('')
    assert not account.is_correct_password('abc')


def test_password_is_hidden():
    password = 'FPak18@PQL91+'
    account = Account('r0077643', password)
    assert not hasattr(account, 'password')
    assert hasattr(account, '_Account__password')
