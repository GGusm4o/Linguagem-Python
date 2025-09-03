# Exibe a soma a média, o maior e o menor valor digitados

resp = 'S'
media = quant = soma = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média entre eles foi {:.2f}'.format(quant, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))