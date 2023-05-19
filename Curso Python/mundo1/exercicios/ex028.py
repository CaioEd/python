# JOGO DA ADiVINHAÇÃO
import random

print('Vou pensar em um número de 0 a 5. Tente adivinhar')

num = random.randint(0,5)

num2 = int(input('Em que número pensei ? '))

if num == num2:
    print('Parabéns você acertou! \n Pensei no número {}' .format(num))
else:
    print('Você errou! Pensei no número {} não no {}' .format(num, num2))

print('--FIM--')