def aumenta(preço=0, taxa=0):
    """
    -> Calcula o aumento de um determinado preço.
    :param preço: O preço que se quer reajustar.
    :param taxa: Qual a porcentagem do aumento.
    :return: O valor reajustado.
    """
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço=0, taxa=0):
    """
    -> Calcula o desconto de um determinado preço.
    :param preço: O preço que se quer diminuir.
    :param taxa: Qual a porcentagem do desconto.
    :return: O valor reajustado.
    """
    res = preço - (preço * taxa/100)
    return res


def dobro(preço=0):
    """
    -> Calcula o dobro de um determinado preço.
    :param preço: O preço que se quer dobrar.
    :return: O dobro do preço.
    """
    res = preço * 2
    return res
    

def metade(preço=0):
    """
    -> Calcula a metade de um preço.
    :param preço: O valor a ser dividido.
    :return: A metade do valor.
    """
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    """
    -> Formata um valor numérico como uma string de moeda.
    :param preço: O valor a ser formatado.
    :param moeda: O símbolo monetário a ser usado (ex: 'R$').
    :return: Uma string formatada do valor (ex: 'R$100,00').
    """
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')
