jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do jogador: '))
totalPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))

for c in range(0, totalPartidas):
    partidas.append(int(input(f'Quantos gols na {c+1}° partida ? ')))

jogador['gols'] = partidas[:]
jogador['total gols'] = sum(partidas)

print('=-'*30)

print(jogador)

print('=-'*30)

for k, v in jogador.items():
    print(f'{k} é {v}')

print(f'O jogador {jogador["nome"]} jogou {totalPartidas} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'Na {i+1}° partida marcou {v} gols.')