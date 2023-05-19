# TIMES DE FUTEBOL - TUPLA COM 10 PRIMEIROS TIMES DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL NA ORDEM DE COLOCAÇÃO E DEPOIS MOSTRE: A) OS 4 PRIMEIROS; B) OS 4 ÚLTIMOS; C) OS TIMES EM ORDEM ALFABÉTICA; D) EM QUE POSIÇÃO ESTÁ O FLUMINENSE

times = ('Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Athletico-PR', 'Atlético-MG', 'Santos', 'Fortaleza', 'Flamengo', 'São Paulo')

print('CAMPEONATO BRASILEIRO')
print('=====================')

print(f'Classificação: {times}')

print('=====================')

print(f'{times[0:4]} estão no G4.')

print(f'{times[6:]} são os 4 últimos.')

print('=====================')

print(f'Os times em ordem alfabética: {sorted(times)}')

print('=====================')

print(f'O fluminense está na {times.index("Fluminense")+1}° posição')