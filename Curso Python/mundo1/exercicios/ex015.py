# SISTEMA ALUGUEL DE CARROS

# O carro custa R$ 60 por dia
# O custo por km rodado é R$ 0,50

quantDias = int(input('Por quantos dias o carro foi alugado?'))
kmRodados = float(input('Quantos quilômetros o carro percorreu ?'))

totalPagar = (60*quantDias) + (0.50*kmRodados)

print('O total a pagar é R$ {}' .format(totalPagar))
