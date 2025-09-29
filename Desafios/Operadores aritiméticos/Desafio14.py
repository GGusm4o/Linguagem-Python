#Converte graus em fahrenheit

graus = float(input("Digite o valor da temperatura em °C: "))
f = 9 * graus / 5 + 32
print('A temperatura de {}°C corresponde a {}°F'.format(graus, f))