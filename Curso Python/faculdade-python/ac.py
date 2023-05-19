"""
from time import sleep

dias = 7

while dias > 0:
    for h in range(24):
        for m in range(60):
            for s in range(60):
                print(f'{h:02}:{m:02}:{s:02}')
                sleep(0.1)
    dias += 1
"""

'''
x=0

while x <= 10:
    y = 0
    
    while y <= 10:
        print('{} x {} = {}' .format(x, y, x*y))
        y += 1
    x += 1
    print()
'''

"""
x = int(input('Número: '))
y = int(input('Segundo número: '))

i = 0

while i<x:
    print('Bom dia')
    j = 0
    while j<y:
        print('Boa tarde')
        j +=1
    i += 1
print('Boa noite')
"""

"""
tab = 1

while tab <= 5:
    i= 1
    while i<=10:
        print(f'{tab} x {i} = {tab*i}')
        i = i+1
    tab = tab+1
"""

"""
i = 10

while i>= 0:
    print(i)
    i -= 1
print('Fogo!')

"""

