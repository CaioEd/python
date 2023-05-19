pessoas = []
dados = []

maior = 0
menor = 0

while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))

    dados.append(nome)
    dados.append(peso)

    pessoas.append(dados[:])
    dados.clear()

    cont = str(input('Quer continuar ? [S/N]')).strip().upper()[0]

    if cont in 'N':
        break

for c in range(0, len(pessoas)):
    if c == 0:
         maior = menor = pessoas[c][1]
    else:
        if pessoas[c][1] > maior:
            maior = pessoas[c][1]
        if pessoas[c][1] < menor:
            menor = pessoas[c][1]

print(f'Foram cadastradas {len(pessoas)} pessoas.')

print(f'O maior peso cadastrado foi {maior} das pessoas: ', end='' )
for i, p in enumerate(pessoas):
    if p[1] == maior:
        print(f'{i}...', end='')

print(f'O menor peso cadastrado foi {menor} das pessoas: ', end='')
for i, p in enumerate(pessoas):
    if p[1] == menor:
        print(f'{i}...', end='')