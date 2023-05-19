# Programa que tem uma função que recebe como parâmetro um vetor e um número n. A função deve retornar a primeira posição onde o número é encontrado ou -1 caso não encontre.

vet = [9, 11, 45, 60, 10]

num = int(input('Digite o número a ser encontrado: '))

def busca(v, n, tam):
    i = 0
    while i < tam:
        if vet[i] == n:
            return i
        i= i+1
    return -1

pos = busca(vet, num, 5)
if pos == -1:
    print('Valor não encontrado!')
else:
    print(f'Valor {num} encontrado!')