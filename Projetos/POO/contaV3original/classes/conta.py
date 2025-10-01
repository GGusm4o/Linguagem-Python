class Conta:

    __total_contas = 0

    @classmethod
    def get_total_contas(cls):
        return cls.__total_contas

    @staticmethod
    def nome_banco():
        return "Banco GG"

    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        type(self).__total_contas += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Saldo inválido")
        else:
            self.__saldo = valor

    def sacar(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            return True

    def gerar_saldo(self):
        print(f'Conta: {self.__numero}')
        print(f'Saldo: {self.__saldo:.10.2f}')