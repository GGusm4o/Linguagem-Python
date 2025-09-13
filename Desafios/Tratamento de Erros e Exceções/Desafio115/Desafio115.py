from lib.interface import *
from lib.file import *
from time import sleep

arq = 'dados.txt'

if not fileExiste(arq):
    criarFile(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de uma arquivo!
        lerFile(arq)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        print(f'{nome} cadastrado com sucesso')
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)