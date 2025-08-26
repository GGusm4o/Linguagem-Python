# Jogo de adivinhação
from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('NÃO FEZ O MÍNIMO! Você conseguiu me vencer!')
else:
    print('Você errou KKKKK! Eu pensei no número {}.'.format(computador))