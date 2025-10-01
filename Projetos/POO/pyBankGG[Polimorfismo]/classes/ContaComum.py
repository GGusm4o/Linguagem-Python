from classes.ContaCliente import ContaCliente


class ContaComum(ContaCliente):

    def __init__(self, numero, IOF, IR, valor_investido, taxa_redimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_redimento)

    def calcular_rendimento(self):
        remuneracao = self.valor_investido * self.taxa_redimento
        valorIOF = remuneracao * self.IOF
        self.valor_investido += remuneracao - valorIOF