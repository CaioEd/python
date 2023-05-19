# NÚMERO POR EXTENSO - PROGRAMA QUE TEM UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM DE 0 ATÉ 10. O PROGRAMA LE UM NÚMERO PELO TECLADO (ENTRE 0 E 10) E MOSTRA POR EXTENSO.

num = int(input('Digite um número entre 0 e 10: '))

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

while num < 0 or num > 10:
        num = int(input('Tente novamente. Digite um número entre 0 e 10: '))
print(f'Você digitou o número {numeros[num]}')
    