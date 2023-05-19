# FAÇA UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E MOSTRE SE ELA COMEÇA COM SANTO OU NÃO

cidade = str(input('Em qual cidade você nasceu ?'))
cidade2 = cidade.split()
cidade3 = cidade2[0]

print('Santo' in cidade3.title())