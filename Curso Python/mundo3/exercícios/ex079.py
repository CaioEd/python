lista = []

while True:
    num = int(input('Digite um número: '))

    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado!')
    cont = str(input('Quer continuar ? [S/N]')).strip().upper()[0]

    if cont in 'N':
        break

lista.sort()
print(f'Lista dos números digitados em ordem crescente{lista}')
