# DICIONÁRIOS

pessoas = {
    'nome': 'Gustavo',
    'idade': 25,
    'sexo': 'Masculino'
}

"""
print(pessoas)
print(pessoas['nome'])
"""

"""
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
"""

"""
del(pessoas['sexo'])

pessoas['peso'] = 100.5

for k, v in pessoas.items():
    print(f'{k} = {v}')
"""

"""
cidade1 = {'nome': 'Itupeva', 'estado': 'São Paulo'}
cidade2 = {'nome': 'Porto Alegre', 'estado': 'Rio Grande do Sul'}

cidades = []

cidades.append(cidade1)
cidades.append(cidade2)

print(cidades)
print(cidades[0]['nome'])
print(cidades[1]['nome'])
"""

estado = {}
brasil = []

for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))

    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')