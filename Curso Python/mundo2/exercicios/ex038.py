# PROGRAMA QUE LE DOIS NÚMEROS INTEIROS E COMPARA ELES MOSTRANDO QUAL VALOR É O MAIOR, QUAL É O MENOR OU SE ELES SÃO IGUAIS 

num1 = int(input('Digite um número inteiro:'))
num2 = int(input('Digite outro número inteiro:'))

if num1 > num2:
    print('O maior número é {} \n O menor é {}' .format(num1, num2))
elif num2 > num1:
    print('O maior número é {} \n O menor é {}' .format(num2, num1))
else:
    print('Os números digitados são iguais.')