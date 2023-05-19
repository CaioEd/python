# MATRIZ


matriz = [[], [], []]

a = 0
b = 0

for c in range(0, 9):
    num = int(input(f'Digite um valor para [{a, b}]: '))

    b += 1

    if a == 0:
        matriz[0].append(num)
    elif a == 1:
        matriz[1].append(num)
    elif a == 2:
        matriz[2].append(num)  

    if b >= 3:
        b = 0
        a += 1

print('=================================')
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ] \n [ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ] \n [ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')


# OUTRA SOLUÇÃO

"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
"""