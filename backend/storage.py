class Storage:
    """
        Classe que armazena os valores de cédulas aceitos,
        bem como a quantidade que se têm de cédulas de cada tipo.
    """

    def __init__(self, bills=[10, 20, 50, 100]):
        self.bills = bills
        # Os valores de cédulas são mantidos em ordem decrescente.
        # Isto garante que o saque retorne o nº mínimo de cédulas.
        self.bills.sort(reverse=True)
        self.available_bills = {bill : 0 for bill in bills}

    def has_bill(self, bill):
        """
            Indica se cédulas do valor {bill} são aceitas.
            @params:
                /bill = um valor inteiro.
        """
        return bill in self.bills

    def deposit(self, bill, count):
        """
            Realiza um depósito de {count} notas de valor {bill}.
            @params:
                /bill  = um valor inteiro
                /count = um valor inteiro
        """
        self.available_bills[bill] += count

    def withdraw(self, value):
        """
            Tenta realizar um saque do valor {value}.
            Se aprovado, retorna um dicionário que indica as cédulas sacadas.
            Se o saque for rejeitado, retorna falso.
            @params:
                /value = um valor inteiro
        """
        # Cria-se um dicionário de notas zerado, e chama-se o método auxiliar.
        used_bills = {bill : 0 for bill in self.bills}
        used_bills = self.__withdraw(value, used_bills)
        # Se o retorno não for falso, então o saque poderá ser realizado.
        if used_bills:
            # Portanto, atualiza-se o registro de notas disponíveis,
            # e então, retorna-se as notas que correspondem ao saque.
            for bill in self.bills:
                self.available_bills[bill] -= used_bills[bill]
            return used_bills
        # Contudo, se uma solução não foi encontrada, então retorna-se falso.
        return False

    def __withdraw(self, value, used_bills):
        """
            Método auxiliar ao método `withdraw`.
            Resolve o problema através de recursão e programação dinâmica.
            Busca pelo menor número de cédulas que completam o valor desejado.
            @params:
                /value      = um valor inteiro
                /used_bills = um dicionário de inteirs para inteiros
        """
        # Se o valor buscado é zero, então retorne a solução atual.
        if value == 0:
            return used_bills
        # Caso contrário, deve-se iterar por todas os valores de notas possíveis...
        for bill in self.bills:
            # Se o valor buscado é maior ou igual ao valor da nota, e se ainda há
            # notas deste valor disponíveis, então...
            if value >= bill and self.available_bills[bill] > used_bills[bill]:
                copy = used_bills.copy()
                copy[bill] += 1
                # Chama-se o método `__withdraw` com o novo valor reduzido.
                # Se o resultado não for falso, encontrou-se a resposta desejada.
                result = self.__withdraw(value - bill, copy)
                if result:
                    return result
        return False
