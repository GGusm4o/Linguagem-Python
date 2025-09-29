# Exibe a tabuada de um número

num = int(input('Digite um número para ver a seu tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'. format(num, c, num*c))