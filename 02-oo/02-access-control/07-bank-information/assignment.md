# CHALLENGE
Complete the BankAccount class.

## CONSTRUCTOR
Initialize private instance variables `__account_number` to `account_number`, and `__balance` to `initial_balance`.

## PUBLIC GETTERS
Define getter methods `get_account_number`, and `get_balance` that return the values of the private variables.

## DEPOSIT METHOD
It should accept an `amount` as input and add it to the account `balance`.

If the deposit amount isn't positive, it should `raise` a `ValueError` exception with the message `Cannot deposit zero or negative funds`. Otherwise, it should add the amount to the balance.

## WITHDRAW METHOD
It should accept an `amount` and check if there is enough money in the account for the withdrawal.

If the withdrawal amount isn't positive, it should `raise` a `ValueError` exception with the message `Cannot withdraw zero or negative funds`. Then, if there are not enough funds it should `raise` a `ValueError` exception with the message `Insufficient funds`. Otherwise, it should deduct the `amount` from the balance.