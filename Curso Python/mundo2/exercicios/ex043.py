# PROGRAMA IMC
# PROGRAMA QUE LE O PESO E A ALTURA DE UMA PESSOA E CALCULA SEU ÍNDICE DE MASSA CORPORAL (IMC). DEPOIS DISSO O PROGRAMA MOSTRA O STATUS DA PESSOA

peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))

imc = peso/(altura*altura)

if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso ideal.' .format(imc))
elif imc >= 18.5 and imc <=25:
    print('Seu IMC é {:.1f} e você está com o peso ideal. Parabéns!' .format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso. Cuidado!' .format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f} e você está com obesidade. Procure ajuda' .format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida. Procure ajuda urgentemente!!!' .format(imc))
