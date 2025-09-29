# Exibe a tabuada de um número v3.0

while True:
    num = int(input('Digite um número para ver a tabuada [número negativo encerra]: '))
    print('-' * 30)
    if num < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 30)
print('PROGRAMA ENCERRADO. Volte sempre!')