from lib.interface import *

def fileExiste(nome):
    try:
        a = open(nome, 'rt') # Abre arquivo de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarFile(nome):
    try:
        a = open(nome, 'wt+') # Cria arquivo de texto
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerFile(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO na hora de escrever!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

