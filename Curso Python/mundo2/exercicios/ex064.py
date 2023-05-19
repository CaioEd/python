#  PROGRAMA QUE LE VÁRIOS NÚMEROS INTEIROS. o PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR [999]. NO FINAL, VAI MOSTRAR QUANTOS NÚMEROS FORAM DIGITADOS E A SOMA ENTRE ELES.

num = int(input('Digite um número inteiro [999 para parar]: '))

numDigitados = 0

while num != 999:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    
    numDigitados =+ numDigitados+1

print('Foram digitados {} números.' .format(numDigitados))
print('====== FIM ======')