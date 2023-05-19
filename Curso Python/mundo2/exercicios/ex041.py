# CATEGORIA DO ATLETA
# ESTE PROGRAMA LE A IDADE QUE O USUÁRIO DIGITOU E MOSTRA QUAL CATEGORIA ELE PERTENCE DE ACORDO COM A IDADE

nome = str(input('Digite seu nome:'))
anoNasc = int(input('Digite o ano que você nasceu:'))

idade = 2023 - anoNasc

if idade >= 6 and idade <= 9:
    print('O atleta {} tem {} anos e está na categoria MIRIM' .format(nome, idade))
elif idade > 9 and idade <=14:
    print('O atleta {} tem {} anos e está na categoria INFANTIL' .format(nome, idade))
elif idade > 14 and idade <= 19:
    print('O atleta {} tem {} anos e está na categoria JÚNIOR' .format(nome, idade))
elif idade > 19 and idade <=25:
    print('O atleta {} tem {} anos e está na categoria SÊNIOR' .format(nome, idade))
elif idade > 25:
    print('O atleta {} tem {} anos e está na categoria MASTER' .format(nome, idade))
elif idade < 6 and idade >= 0:
    print('Está pessoa não tem idade suficiente para entrar em uma categoria')
else:
    print('Dados inválidos')
