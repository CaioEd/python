pessoa = {}
pessoas = []
soma = media = 0
mulheres = []
acimaM = []

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo (M/F): '))
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    pessoas.append(pessoa.copy())

    continuar = str(input('Quer continuar ? [S/N]')).strip().upper()[0]

    if continuar in 'N':
        break 
    
print('-='*30)

print(f'Foram cadastradas {len(pessoas)} pessoas.')
media = soma/ len(pessoas)
print('A média de idade é {:.1f}' .format(media))

for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])

for i in pessoas:
    if i['idade'] > media:
        acimaM.append(i['nome'])

print(f'As mulheres cadastradas foram {mulheres}')
print(f'Lista de pessoas acima da média: {acimaM}')
