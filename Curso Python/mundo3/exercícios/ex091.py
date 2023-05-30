from random import randint
from time import sleep
from operator import itemgetter

maior = menor = 0

jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = []

for k,v in jogadores.items():
    print(f'O jogador {k} tirou o valor {v} no dado')
    sleep(0.8)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')