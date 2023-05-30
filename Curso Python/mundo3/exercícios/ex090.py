aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))

if aluno['média'] < 6.0:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

print('-=' * 30)

for k, v in aluno.items():
    print(f'{k} é {v}')