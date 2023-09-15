from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class InsufficientBalanceError(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit


class Account:
    """
    Account is a class.
    Members: i) attributes ii) methods: constructor (__init__)
    """

    def __init__(self, iban, balance=0, status=AccountStatus.ACTIVE):
        """
        constructor
        :param iban: international bank account number, unique
        :param balance: float
        :param status:  ACTIVE, CLOSED, BLOCKED
        """
        self.iban = iban
        self.balance = balance
        self.status = status

    # business method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("You must provide a positive amount to deposit")
        self.balance += amount

    # business method
    def withdraw(self, amount):
        # validation
        if amount <= 0:
            raise ValueError("You must provide a positive amount to withdraw")
        # business rule
        if amount > self.balance:
            deficit = amount - self.balance
            raise InsufficientBalanceError("Your balance does not cover your expenses", deficit)
        self.balance -= amount


# an object is created!
acc1 = Account("tr1", 1_000_000)
acc2 = Account("tr2", 2_000_000)
try:
    acc1.deposit(50_000)
    acc1.deposit(25_000)
    acc2.withdraw(75_000)
    acc2.withdraw(10_000_000)
except InsufficientBalanceError as e:
    print(e.message, e.deficit)
