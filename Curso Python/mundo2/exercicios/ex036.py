# APROVANDO EMPRÉSTIMO
# PROGRAMA QUE PERGUNTA O VALOR DE UMA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR. A PRESTAÇÃO MENSAL NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

valorCasa = float(input('Digite o valor da casa:'))
salario = float(input('Digite seu salário:'))
quantAnos = int(input('Em quantos anos você quer pagar:'))

anosPmeses = quantAnos*12
prestacaoPmes = valorCasa/anosPmeses

if prestacaoPmes > (30*salario)/100:
    print('Para pagar a casa de R$ {} em {} anos o valor das prestações será de {:.1f} por mês \n Empréstimo NEGADO!' . format(valorCasa, quantAnos, prestacaoPmes))
else:
    print('Para pagar a casa de R$ {} em {} o valor das prestações será de {:.1f} por mês \n Empréstimo APROVADO!' . format(valorCasa, quantAnos, prestacaoPmes))