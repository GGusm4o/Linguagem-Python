import datetime
from classes.Extrato import Extrato


class Conta:

    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPÓSITO", valor, datetime.date.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False  # Não tem saldo suficiente
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, datetime.date.today()])
            return True  # Saque realizado com sucesso

    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERÊNCIA", valor, datetime.date.today()])
            return "Transferência Realizada"

    def gerar_saldo(self):
        print(f"Conta {self.numero}")
        print(f"Saldo: R${self.saldo:10.2f}")
