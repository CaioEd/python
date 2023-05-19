# PROGRAMA QUE LE 5 VALORES E GUARDA ELES EM UMA LISTA. NO FINAL MOSTRA QUAL FOI O MAIOR E O MENOR NÚMERO DIGITADO DA LISTA

valores = []

maior = 0
menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um número inteiro para a posição {c}: ')))

    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]


print(valores)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
