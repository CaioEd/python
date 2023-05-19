# CATETO OPOSTO, CATETO ADJACENTE E HIPOTENUSA

from math import hypot

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite ocomprimento do cateto adjacente: '))

comprimentoHipot = hypot(catetoOposto, catetoAdjacente)

print('O comprimento da hipoteusa é: {:.2f}' .format(comprimentoHipot))