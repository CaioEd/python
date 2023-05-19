numeros = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    cont = str(input('Quer continuar ? [S/N]')).strip().upper()[0]

    if cont in 'N':
        break

print(numeros)
print(f'Foram digitados {len(numeros)} números. ')
numeros.sort(reverse=True)
print(f'Lista na ordem decrescente {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista')
else:
    print('5 não está na lista')