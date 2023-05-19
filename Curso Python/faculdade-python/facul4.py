# ESTRUTURAS DE REPETIÇÃO ANINHADAS

# COMANDO BREAK - Programa que recebe um número e exibe se é primo ou não

'''
n = int(input('Digite um número:'))
divisor = 2

while divisor < n:
    if n%divisor == 0:
        break
    divisor += 1

if divisor == n:
    print('Este número é primo')
else:
    print('Este número não é primo')

'''

# REPEAT...UNTIL 

# PROGRAMA QUE RECEBE UM VALOR E CALCULA A RAIZ QUADRADA DELE. ENQUANTO O VALOR RECEBIDO FOR NEGATIVA O PROGRAMA REPETE A SOLICITAÇÃO


'''
from math import sqrt

while True:
    n = float(input('Digite um número:'))
    if n>=0: break
print('A raiz quadrada de {} é {:.2f}' .format(n, sqrt(n)))
'''

# LAÇOS ANINHADOS
# Programa que cria uma função que simula um relógio exibindo desde 00:00:00 até 23:59:59

def relogio():
    minuto = 0
    while minuto < 60:
        segundo = 0
        while segundo < 60:
            print(f'{0:02}:{minuto:02}:{segundo:02}')    #{0:02} mostra 0 na tela duas vezes
            segundo += 1
        minuto += 1

relogio()