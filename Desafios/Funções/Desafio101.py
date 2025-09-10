# Exibe se o voto é obrigatorio, opcional ou não vota
def voto():
    from datetime import date
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
print('-' * 32)
print(voto())
