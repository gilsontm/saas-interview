from backend.utils import tests
from backend.controller import Controller

def example():
    # Instancia o controlador do caixa.
    controller = Controller()
    # Deposita algumas cédulas.
    controller.deposit(100, 2)
    controller.deposit( 50, 4)
    controller.deposit( 10, 3)
    # Saca 110 reais.
    bills = controller.withdraw(110)
    print(f"Cédulas de R$100: {bills[100]}.") # 1
    print(f"Cédulas de R$ 50: {bills[ 50]}.") # 0
    print(f"Cédulas de R$ 20: {bills[ 20]}.") # 0
    print(f"Cédulas de R$ 10: {bills[ 10]}.") # 1
                                              # no total: 100 + 10 = 110 reais


def main():
    print(f"[TEST 1]: {'PASSED' if tests.test1() else 'FAILED'}.")
    print(f"[TEST 2]: {'PASSED' if tests.test2() else 'FAILED'}.")
    print(f"[TEST 3]: {'PASSED' if tests.test3() else 'FAILED'}.")

if __name__ == "__main__":
    main()
