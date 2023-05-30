# FUNÇÕES - PARTE 2

"""
help()
"""

"""
def contador(i, f, p):
    
    manual função
    


help(contador)
"""

"""
def somar(a=0, b=0, c=0):
    s = a+b+c
    print(f'A soma vale {s}')


somar(2, 6)
somar(b=6, c=2)
"""

# ESCOPO VARIÁVEIS

"""
def teste():
    x = 2 # VARIÁVEL DE ESCOPO LOCAL - SÓ VALE NA FUNÇÃO
    n = 10
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

def teste2():
    global n
    n += 20
    print(f'Na função teste2 n global passa a valer {n}')


n = 1
print(f'No programa principal n vale {n}')

teste()
teste2()
"""

"""
def somar(a, b, c):
    s = a+b+c
    return s


r1 = somar(4, 7, 2)
r2 = somar(3, 12, 20)
r3 = somar(21, 232, 101)

print(f'Os resultados dos cálculos foram: {r1}, {r2}, {r3}')
"""

def fatorial(num=1):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    return fat


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')