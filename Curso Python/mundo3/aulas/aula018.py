# LISTAS - PARTE 2

"""

pessoas = [['Caio', 19], ['Guanabara', 46]]
dados = ['Pedro', 25]

pessoas.append(dados[:])


print(pessoas)
print(pessoas[0][0])



for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos')

"""

galera = []
dado = []

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >=18:
        print(f'{pessoa[0]} é maior de idade')