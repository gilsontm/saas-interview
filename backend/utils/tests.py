from backend.utils import exceptions
from backend.controller import Controller


def test1():
    """ Funcionamento geral: depósito, saque e integridade. """
    try:
        controller = Controller()

        # Não consegue sacar 60 reais, pois não há dinheiro no caixa.
        assert(not controller.withdraw(60))

        # Realizar depósito.
        controller.deposit(100, 1)
        controller.deposit( 50, 1)
        controller.deposit( 20, 3)

        # Checar depósito.
        bills = controller.storage.available_bills
        assert(bills[100] == 1)
        assert(bills[ 50] == 1)
        assert(bills[ 20] == 3)
        assert(bills[ 10] == 0)

        # Realizar e checar saque.
        bills = controller.withdraw(60)
        assert(bills)
        assert(bills[100] == 0)
        assert(bills[ 50] == 0)
        assert(bills[ 20] == 3) # Foram sacados 60 reais (3 notas de 20 reais).
        assert(bills[ 10] == 0)

        # Checar notas disponíveis.
        bills = controller.storage.available_bills
        assert(bills[100] == 1)
        assert(bills[ 50] == 1)
        assert(bills[ 20] == 0)
        assert(bills[ 10] == 0)

        # Não consegue sacar 80 reais, pois há somente notas de 50 e 100 reais.
        assert(not controller.withdraw(80))
    except Exception as ex:
        print(ex)
        return False
    return True


def test2():
    """ Preferência por notas maiores. """
    try:
        controller = Controller()
        # Realiza depósito.
        controller.deposit(50, 1)
        controller.deposit(20, 3)
        controller.deposit(10, 1)

        # É preferível sacar uma nota de 50 e uma de 10, invés de três de 20 reais.
        bills = controller.withdraw(60)
        assert(bills)
        assert(bills[100] == 0)
        assert(bills[ 50] == 1) # Uma nota de 50 reais.
        assert(bills[ 20] == 0)
        assert(bills[ 10] == 1) # Uma nota de 10 reais.

        # Só então as notas de 20 reais serão sacadas.
        bills = controller.withdraw(60)
        assert(bills)
        assert(bills[100] == 0)
        assert(bills[ 50] == 0)
        assert(bills[ 20] == 3) # Três notas de 20 reais.
        assert(bills[ 10] == 0)

        # Por fim, não há mais dinheiro; então o saque é rejeitado.
        bills = controller.withdraw(60)
        assert(not bills)
    except Exception as ex:
        print(ex)
        return False
    return True


def test3():
    """ Não aceitar notas com valores desconhecidos, nem aceitar valores negativos."""
    score = 0

    # Depósito com número de cédulas inválido.
    try:
        controller = Controller()
        # Tenta depositar duas cédulas e meia.
        controller.deposit(100, 2.5)
    except exceptions.InvalidBillCount:
        score += 1

    # Depósito com valor de cédula inválido.
    try:
        controller = Controller()
        # Tenta depositar um cédula de valor 3000.
        controller.deposit(3000, 2)
    except exceptions.InvalidBillValue:
        score += 1

    # Saque de valor negativo.
    try:
        controller = Controller()
        controller.deposit(100, 2)
        controller.deposit( 10, 7)
        # Tenta sacar o valor -30 reais.
        controller.withdraw(-30)
    except exceptions.InvalidNegativeValue:
        score += 1

    return score == 3
