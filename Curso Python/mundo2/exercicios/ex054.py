# PROGRAMA QUE LE O ANO DE NASCIMENTO DE 4 PESSOAS E NO FINAL MOSTRA QUANTAS JÁ ATINGIRAM A MAIORIDADE E QUANTAS AINDA NÃO.

somaMaiores = 0
somaMenores = 0

for c in range(1,7):
    anoNasc = int(input('Qual o ano de nascimento da {}° pessoa: ' .format(c)))
    if anoNasc <= 2005:
        somaMaiores = somaMaiores + 1
    else:
        somaMenores = somaMenores + 1
print('{} pessoas são maiores de idade e {} são menores.' .format(somaMaiores, somaMenores))