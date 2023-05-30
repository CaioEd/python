def fichaJogador(nome='<desconhecido>', gols=0):
    print (f'O jogador {nome} marcou {gols} gols no campeonato.')


nomeJogador = str(input('Nome do jogador: '))
golsJogador = str(input('Gols: '))  # string deixa ficar vazio

if golsJogador.isnumeric():
    golsJogador = int(golsJogador)
else:
    golsJogador = 0

if nomeJogador.strip() == '':
    fichaJogador(gols=golsJogador)
else:
    fichaJogador(nomeJogador, golsJogador)