# Exibe uma ficha de um jogador
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

#Programa Principal
nome = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gol=g)
else:
    ficha(nome, g)