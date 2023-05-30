def area(largura, altura):
    a = largura*altura
    print(f'A área do terreno de {largura}x{altura} é igual a {a}m²')


larg = float(input('LARGURA terreno (m): '))
alt = float(input('ALTURA do terreno (m): '))

area(larg, alt)