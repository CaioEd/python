# PROGRAMA QUE LE 6 NÚMEROS INTEIROS E FAZ A SOMA APENAS DAQUELES  QUE FOREM PARES.

soma = 0
for c in range(1,7):
    num = int(input('Digite um número:'))
    if num%2 == 0:
        soma = soma + num
print('A soma dos números digitados que são pares é {}' .format(soma))