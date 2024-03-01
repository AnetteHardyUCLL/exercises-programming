class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, another_amount):
        if another_amount.currency == self.currency:
            return Money((self.amount + another_amount.amount), self.currency)
        else:
            raise RuntimeError("Mismatch currencies!")

    def __sub__(self, another_amount):
        if another_amount.currency == self.currency:
            return Money((self.amount - another_amount.amount), self.currency)
        else:
            raise RuntimeError("Mismatch currencies!")

    def __mul__(self, number):
        return Money(self.amount * number, self.currency)
