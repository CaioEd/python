# Dobro, Triplo e raiz quadrada
from math import sqrt

num = float(input('Digite um número:'))

numDob = num*2
numTri = num*3
numRaQua = sqrt(num)

print('O dobro, triplo e raiz quadrada de {} são respectivamente: {}, {} e {:.1f}.' .format(num, numDob, numTri, numRaQua))