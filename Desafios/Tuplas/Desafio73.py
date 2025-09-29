# Exibe a Tabela do Brasileirão

times = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo', 'Red Bull Bragantino', 'Fluminense','Internacional', 'Ceará', 'Corinthians', 'Grêmio', 'Atlético-MG', 'Vasco da Gama', 'Santos', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')
print('-='*15)
print(f'Lista de times do BRASILEIRÃO: {times}')
print('-='*15)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos times são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Vasco da Gama está na posição: {times.index("Vasco da Gama")+1}° posição')