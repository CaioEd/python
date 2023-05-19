numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    cont = str(input('Quer continuar ? [S/N]')).strip().upper()[0]

    if cont in 'N':
        break
print(f'A lista completa de números é: {numeros}')
print(f'A lista dos números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')