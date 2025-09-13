def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n
        
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

#Programa Principal
n = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'Você acabou de digitar o número {n}')