# Converte uma medida em metros para Centímetros e Milímetros

medida = float(input('Digite um valor em metros: '))
centimetros = medida * 100
milimetros = medida * 1000
print('A medida de {}m corresponde a {}cm, {:.0f}mm'.format(medida, centimetros, milimetros))
