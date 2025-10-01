from classes.Conta import Conta
from classes.Poupanca import Poupanca


class ContaRemuneradaPoupanca(Conta, Poupanca):

    def __init__(self, cliente, numero, saldo, taxa_remuneracao):
        Conta.__init__(self, cliente, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)

    def remuneracaoConta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30)