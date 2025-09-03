# Jogo de adivinhação melhorado
from random import randint

computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Acertou com {} palpites. Parabéns!'.format(palpite))
