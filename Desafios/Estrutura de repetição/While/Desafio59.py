# Exibe um menu de opções
from time import sleep
def carregamento():
    total = 50
    for i in range(total + 1):
        porcentagem = int((i / total) * 100)
        barra = '#' * (porcentagem // 5)
        espacos = ' ' * ((100 - porcentagem) // 5)
        print('\rProgresso: [{}{}] {}%'.format(barra, espacos, porcentagem), end='')
        sleep(0.1)
        
carregamento()
print()
print('=-=' * 13)
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
opção = 0
carregamento()
print()
print('=-=' * 13)
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é: {}'.format(num1, num2, soma))
    elif opção == 2:
        produto = num1 * num2
        print('O resultado entre {} X {} é: {}'.format(num1, num2, produto))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {}, o maior é: {}'.format(num1, num2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    print()
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre!')