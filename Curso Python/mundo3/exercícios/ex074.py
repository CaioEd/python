# PROGRAA QUE GERA 5 NÚMEROS ALEATÓRIOS E COLOCA EM UMA TUPLA. DEPOIS DISSO, MOSTRA ANLISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDICA O MENOR E O MAIOR VALOR GERADO.

import random

numeros = (random.randint(0, 99), random.randint(0, 99), random.randint(0, 99), random.randint(0, 99), random.randint(0, 99))

numerosOrdem = sorted(numeros)

print(f'Os números sorteados foram {numeros}')
print(f'O maior número é {numerosOrdem[4]}')
print(f'O menor número é {numerosOrdem[0]}')