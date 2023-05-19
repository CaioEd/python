# ESTRUTURA DE REPETIÇÃO WHILE
'''
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim') 

'''

'''
    resposta = "S"

while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar ? [S/N]')).upper()
print('FIM')

'''

n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um número: '))

    if n%2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} ímpares!' .format(par, impar))