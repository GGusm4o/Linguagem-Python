# Exibe 5 valores numéricos e guarde-os em uma lista

listaNum = []
maior = 0
menor = 0
for cont in range(0, 5):
    listaNum.append(int(input(f'Digite um valor para a Posição {cont}: ')))
    if cont == 0:
        maior = menor = listaNum[cont]
    else:
        if listaNum[cont] > maior:
            maior = listaNum[cont]
        if listaNum[cont] < menor:
            menor = listaNum[cont]
print('=-' * 30)
print(f'Você digitou os valores {listaNum}')
print(f'O maior valor foi {maior} na posição ', end='')
for i, v in enumerate(listaNum):
    if v == maior:
        print(f'{i}°...', end='')
print()
print(f'O menor valor foi {menor} na posição ', end='')
for i, v in enumerate(listaNum):
    if v == menor:
        print(f'{i}°...', end='')
print()