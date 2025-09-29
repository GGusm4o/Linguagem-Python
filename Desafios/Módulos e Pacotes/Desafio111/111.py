#Criação melhorada de modulo para calcular a metade, o dofrom
from utilidaescev import moeda

p = float(input('Digite o preço: R$'))
a = int(input('Digite a porcentagem de aumento: '))
r = int(input('Digite a porcentagem de redução: '))
moeda.resumo(p, a, r)