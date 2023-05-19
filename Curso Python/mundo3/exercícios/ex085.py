lista = [[], []]

for c in range(0,5):
    num = int(input('Digite um número: '))

    if num%2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()

print(f'Os números pares da lista são {lista[0]}')
print(f'Os números ímpares da lista são {lista[1]}')

    