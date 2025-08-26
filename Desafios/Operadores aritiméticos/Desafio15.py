# Verifica o aluguel de carro com base nos dias e km rodados

dias = int(input('Quantos dias o carro foi alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))