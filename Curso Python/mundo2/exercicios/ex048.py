# PROGRAMA QUE CALCULA A SOMA ENTRE TODOS OS NÚMEROS QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM ENTRE 1 E 500

soma = 0
contador = 0

for c in range(1, 501, 2):
    if c%3 == 0:
        contador = contador + 1
        soma = c + soma
print('A soma de todos os valores {} números é {}:' .format(contador, soma))