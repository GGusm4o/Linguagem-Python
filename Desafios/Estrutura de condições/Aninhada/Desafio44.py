# Exibe as formas de pagamento de uma loja

print('{:=^40}'.format('\033[1;32m LOJAS GG \033[m'))
preço = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro
[ 2 ] À vista cartão
[ 3 ] 2x ou mais no cartão
[ 4 ] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))  
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('A compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('A compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preço
    print('\033[1;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')

print('A compra de R${:.2f} vai custar R${:.2f}'.format(preço, total))