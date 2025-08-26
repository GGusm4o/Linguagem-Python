# Exibe um sálario com um aumento de 15% de desconto

salario = float(input('Qual é o salario do funcionário: R$ '))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de desconto ganhará R${:.2f}'.format(salario, aumento))