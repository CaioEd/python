# VERIFICAR SE O NÚMERO NATURAL É PAR

n = int(input('Digite um número: '))

if not (n % 2 == 1) :
    print('{} é par!' .format(n))
else:
    print('{} é ímpar!' .format(n))

