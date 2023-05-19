# LISTAS

"""

num = [2, 5, 10, 24]

num.append(44)

print(num)

num.pop()
num.remove(5)

print(num)

num.insert(0, 77)

print(num)

"""

"""
valores = [33, 5, 8, 987, 4]

print(len(valores))

num.sort

print(valores)
"""

"""
valores = [2, 5, 9, 1]

if 4 in valores:
    valores.remove(5)
else:
    print('Não achei o número 4')

for valor in valores:
    print(f'{valor}...')

for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor}')
"""

valores = []

for cont in range(0, 4):
    valores.append(int(input('Digite um número: ')))

print(valores)