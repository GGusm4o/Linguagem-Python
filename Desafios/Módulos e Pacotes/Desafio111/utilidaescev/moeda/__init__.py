def aumenta(preço=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço.
    :param preço: O preço que se quer reajustar.
    :param taxa: Qual a porcentagem do aumento.
    :return: O valor reajustado.
    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Calcula o desconto de um determinado preço.
    :param preço: O preço que se quer diminuir.
    :param taxa: Qual a porcentagem do desconto.
    :return: O valor reajustado.
    """
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    -> Calcula o dobro de um determinado preço.
    :param preço: O preço que se quer dobrar.
    :return: O dobro do preço.
    """
    res = preço * 2
    return res if formato is False else moeda(res)
    

def metade(preço=0, formato=False):
    """
    -> Calcula a metade de um preço.
    :param preço: O valor a ser dividido.
    :return: A metade do valor.
    """
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    -> Formata um valor numérico como uma string de moeda.
    :param preço: O valor a ser formatado.
    :param moeda: O símbolo monetário a ser usado (ex: 'R$').
    :return: Uma string formatada do valor (ex: 'R$100,00').
    """
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumenta(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 35)