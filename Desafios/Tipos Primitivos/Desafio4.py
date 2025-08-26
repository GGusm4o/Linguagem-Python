# Verifica se o dado é número, letra ou Alfanumérico

n = input('Digite algo: ')
print('Numéro: ', n.isnumeric())
print('Alpha: ', n.isalpha())
print('Alfanumérico: ', n.isalnum())