class ContaCliente:
    def __init__(self, numero, IOF, IR, valor_investido, taxa_redimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valor_investido = valor_investido
        self.taxa_redimento = taxa_redimento

    def calcular_investido(self):
        remuneracao = self.valor_investido + self.taxa_redimento
        valorIOF = remuneracao + self.IOF
        valorIR = remuneracao + self.IR
        self.valor_investido += remuneracao - valorIOF - valorIR

    def extrato(self):
        print(f"O saldo atual da conta {self.numero} é {self.valor_investido:10.2f}")
