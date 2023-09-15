from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class InsufficientBalanceError(Exception):
    def __init__(self, message, deficit):
        self.message = message
        self.deficit = deficit

    def __str__(self):
        return f"InsufficientBalanceError [message: {self.message}, deficit: {self.deficit}]"


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
        self._iban = iban
        self._balance = balance
        self._status = status

    def __str__(self):
        return f"Account [iban: {self.iban}, balance: {self._balance}, status: {self._status}]"

    # business method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("You must provide a positive amount to deposit")
        self._balance += amount

    # business method
    def withdraw(self, amount):
        # validation
        if amount <= 0:
            raise ValueError("You must provide a positive amount to withdraw")
        # business rule
        if amount > self._balance:
            deficit = amount - self._balance
            raise InsufficientBalanceError("Your balance does not cover your expenses", deficit)
        self._balance -= amount

    @property
    def iban(self):
        print("reading the property: iban")
        return self._iban

    @property
    def balance(self):
        print("reading the property: balance")
        return self._balance

    @property
    def status(self):
        print("reading the property: status")
        return self._status

    @status.setter
    def status(self, new_status):
        print("setting the property: status")
        if new_status == AccountStatus.CLOSED:
            self._status = new_status


"""
        Account: Base/Super Class
CheckingAccount: Derived/Sub Class
"""


class CheckingAccount(Account):

    def __init__(self, iban, balance=0, status=AccountStatus.ACTIVE, overdraft_amount=1_000):
        super().__init__(iban, balance, status)
        self._overdraft_amount = overdraft_amount

    @property
    def overdraft_amount(self):
        print("reading the property: overdraft_amount")
        return self._overdraft_amount

    def withdraw(self, amount):
        # validation
        if amount <= 0:
            raise ValueError("You must provide a positive amount to withdraw")
        # business rule
        if amount > (self.balance + self.overdraft_amount):
            deficit = amount - self.balance - self.overdraft_amount
            raise InsufficientBalanceError("Your balance does not cover your expenses", deficit)
        self._balance -= amount


# an object is created!
acc1 = CheckingAccount("tr1", 5_000, overdraft_amount=2_000)
acc2 = Account("tr2", 2_000_000)
try:
    acc2.deposit(50_000)
    acc2.deposit(25_000)
    acc1.withdraw(7_000)
    # acc2.withdraw(10_000_000)
    acc2.status = AccountStatus.CLOSED
    # AttributeError: property 'balance' of 'Account' object has no setter
    # acc2.balance = acc1.balance - 100_000_000
    print(f"acc1's balance: {acc1.balance}")
    print(f"acc1: {acc1}")
    acc1.withdraw(1)
except InsufficientBalanceError as e:
    print(e)
