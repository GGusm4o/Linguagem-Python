class Poupanca:

    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao

    def remuneracaoConta(self):
        self.saldo += self.saldo * self.taxa_remuneracao