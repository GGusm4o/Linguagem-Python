# Verifica o dobro, triplo e a raiz de um número

num = int(input('Digite um numero: '))
# d = num * 2
# t = num * 3
# raiz = num ** (1/2)
print('O dobro de {} vale {}.'.format(num, num*2))
print('O triplo de {} vale {}\nA raiz de {} vale {}'.format( num, (num*3), num, pow(num, (1/2))))