# JOGO DA ADVINHAÇÃO: JOGO DO DESAFIO 28 MELHORADO. O COMPUTADOR VAI 'PENSAR' EM UM NÚMERO DE 0 A 10 SÓ QUE AGORA O JOGADOR PODE TENTAR ADVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES ELE DEU.

import random

print('Vou pensar em um número de 0 a 10. Tente adivinhar')

num = random.randint(0,10)

num2 = int(input('Em que número pensei ? '))

somaTentativas = 0

while num2 != num:
    somaTentativas =+ somaTentativas+1 
    print('Você errou! Tente novamente')
    num2 = int(input('Em que número pensei ? '))

print('Parabéns você acertou! O número é {} \n Você teve {} tentativas até acertar.' .format(num, somaTentativas))

print('--FIM--')