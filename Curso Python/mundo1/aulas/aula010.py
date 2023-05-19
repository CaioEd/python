# CONDIÇÕES 

"""
tempo = int(input('Quantos anos tem seu carro ?'))

if tempo <=3:
    print ('Carro novo')
else:
    print('Carro velho')

print('FIM')
"""

n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
n3 = float(input('Digite a nota do seu trabalho:'))

media = (n1 + n2 + n3)/3

print('Sua média foi {:.1f}' .format(media))

if media <= 5.9:
    print('Você está abaixo da média!')
else:
    print('Você está acima da média! Parabéns')
