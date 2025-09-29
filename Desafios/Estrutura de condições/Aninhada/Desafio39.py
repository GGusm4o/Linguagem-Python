from datetime import date

nasc = int(input("Digite o ano de nascimento: "))
Atual = date.today().year
idade = Atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, Atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = Atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = Atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))