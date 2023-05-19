# SISTEMA DE RADAR

print('--- Sistema de Radar ---')

vel = int(input('Qual foi a velocidade do carro ? '))
multa = (vel-80)*7

if vel > 80:
    print('MULTADO \n O motorista ultrapassou o limite de velocidade de 80 km/h! \n O valor da multa será de R$ {}' .format(multa))
else:
    print('Velocidade permitada!')