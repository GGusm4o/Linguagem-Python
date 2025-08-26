# Exibe uma lista em ordem aleatória

from random import shuffle

nome1 = str(input('Digite o nome do primeito do aluno: '))
nome2 = str(input('Digite o nome do segundo do aluno: '))
nome3 = str(input('Digite o nome do terceiro do aluno: '))
nome4 = str(input('Digite o nome do quarto do aluno: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem de apresentação será ')
print(lista)

