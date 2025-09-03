# cadastre-os em uma lista. Número já exista lá dentro, ele não será adicionado

num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não adicionado...')
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
num.sort()
print(f'Você digitou os valores: {num}')