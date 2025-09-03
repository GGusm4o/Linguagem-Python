# Exibe a soma de numeros pares

soma = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você informou {} números PARES e a soma foi {}'.format(count, soma))