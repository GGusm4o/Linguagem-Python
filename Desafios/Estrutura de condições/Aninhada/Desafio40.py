# Verifica a média do aluno

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print('A sua média foi {:.1f}'.format(media))
if media >= 6.0:
    print('Você foi APROVADO!')
elif media >= 5.0:
    print('Você está em RECUPERAÇÃO!')
else:
    print('Você foi REPROVADO!')
