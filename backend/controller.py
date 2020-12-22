from backend.storage import Storage
from backend.utils import exceptions


class Controller:
    """ Encapsula a classe `Storage` e serve de interface para o restante do sistema. """

    def __init__(self):
        self.storage = Storage()

    def deposit(self, bill, bill_count):
        if (bill_count < 0) or not isinstance(bill_count, int):
            raise exceptions.InvalidBillCount()
        if not self.storage.has_bill(bill):
            raise exceptions.InvalidBillValue(bill)
        self.storage.deposit(bill, bill_count)

    def withdraw(self, value):
        if (value < 0):
            raise exceptions.InvalidNegativeValue()
        return self.storage.withdraw(value)
