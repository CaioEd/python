# ANÁLISE DE ANO BISSEXTO

import datetime

print('Análise de ano bissexto \n Digite 0 para considerar o ano atual')

ano = int(input('Digite o ano e descubra se ele é bissexto:'))

if ano == 0:
    ano = datetime.date.today().year

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('{} é um ano bissexto!' .format(ano))
else:
    print('{} não é um ano bissexto!' .format(ano))

    
