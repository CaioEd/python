# PREÇO DA PASSAGEM

print('CALCULE O PREÇO DA SUA PASSAGEM AQUI')

dist = int(input('Qual a distância da sua viagem em km ?'))

viagem200 = dist*0.50
viagemMais200 = dist*0.45

if dist <= 200:
    print('Sua passagem custara R$ {:.1f}' .format(viagem200))
else:
    print('Sua passagem custará R$ {:.1f}' .format(viagemMais200))
