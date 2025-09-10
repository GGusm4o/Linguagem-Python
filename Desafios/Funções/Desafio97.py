# Exibe a função esvrever
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# Programa principal
escreva('Olá, Mundo!')
escreva('Py')
escreva('CeV')