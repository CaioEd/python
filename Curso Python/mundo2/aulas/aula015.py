# INTERRONPENDO REPETIÇÕES WHILE

n = 0
contador = 0
soma = 0

while True:
    n = int(input('Número: [999 - parar]'))
    contador += 1
    if n == 999:
        contador = contador - 1
        break
    soma += n

print(f'A soma de todos os números digitados é {soma}')
print(f'Foram digitados {contador} números')
print('FIM')