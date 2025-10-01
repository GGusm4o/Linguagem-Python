from classes.ContaCliente import ContaCliente


class ContaRemunerada(ContaCliente):

    def __init__(self, numero, IOF, IR, valor_investido, taxa_redimento):
        super().__init__(numero,IOF, IR, valor_investido, taxa_redimento)

    def calcular_rendimento(self):
        self.valor_investido += self.valor_investido * self.taxa_redimento