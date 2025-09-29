# Verifica se a frase é um palíndromo

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
