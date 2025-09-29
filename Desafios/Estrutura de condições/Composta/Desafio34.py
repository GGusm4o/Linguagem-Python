# Verificando o aumento salarial

salário = float(input('Digite o salário do funcionário: R$'))
if salário <= 1250:
    aumento = salário + (salário * 15 / 100)   
else:
    aumento = salário + (salário * 10 / 100)

print('Quem ganhava R${} agora ganhará R${:.2f}'.format(salário, aumento))