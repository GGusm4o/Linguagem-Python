# Exibe o calculo de números pares, terceira coluna e da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0: # 1° Soma dos números pares
            spar += matriz[l][c]
        if c == 0: # 3° O maior valor da segunda linha
            mai = matriz[1][c]
        elif matriz[1][c] > mai:
            mai = matriz[1][c]
    scol += matriz[l][2] # 2° Soma da terceira coluna
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares é {spar}')
print(f'A soma da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {mai}')