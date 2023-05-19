# LER O NOME
# - NOME COM TODAS AS LETRAS MAIÚSCULAS E MINÚSCULAS
# - QUANTAS LETRAS AO TOD
# - QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite seu nome:')).strip()
quant1nome = nome.split()

print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(len(quant1nome[0])) )
