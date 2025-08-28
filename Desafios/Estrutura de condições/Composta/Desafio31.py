# Calcular o preço da passagem

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} km.'.format(distancia))
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 # 1° Forma

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print('O preço da sua passagem será de R$ {:.2f}'.format(preço))