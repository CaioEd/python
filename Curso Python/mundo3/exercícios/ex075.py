# PROGRAMA QUE LE 4 VALORES PELO TECLADO E GUARDA ELES EM UMA TUPLA. NO FINAL MOSTRA: A) QUANTAS VEZES APARECEU O VALOR 9; B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3; C) QUAIS FORAM OS NÚMEROS PARES.

num = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))

numeros = (num, num2, num3, num4)

print(f'Você digitou os valores {numeros}')

print(f'O número 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu na posição {numeros.index(3)}')
else:
    print('O valor 3 não apareceu')

print('Os valores pares digitados foram:')
for numero in numeros:
    if numero%2 == 0:
        print(numero)
