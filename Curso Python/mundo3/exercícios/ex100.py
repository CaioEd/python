from random import randint

valores = []

def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Valores sorteados {valores}')


def somaPar(lista):
    soma = 0

    for valor in lista:
        if valor%2 == 0:
            soma += valor
        
    print(f'O valor da soma dos números pares sorteados é: {soma}')


sorteia(valores)
somaPar(valores)