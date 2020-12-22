class InvalidBillCount(Exception):
    def __init__(self):
        super().__init__(self, "O número de cédulas é inválido.")

class InvalidBillValue(Exception):
    def __init__(self, bill):
        super().__init__(self, f"Não são aceitas notas de valor {bill}.")

class InvalidNegativeValue(Exception):
    def __init__(self):
        super().__init__(self, "Não é permitido sacar um valor negativo.")
