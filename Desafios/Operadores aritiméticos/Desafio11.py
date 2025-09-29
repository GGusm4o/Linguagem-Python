# Verificar a quantidade de tinta para pintar uma parede

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {:.0f}x{:.0f} e sua área é de {}m²' .format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, precisará de {}l de tinta. '.format(tinta))