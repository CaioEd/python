# FUNÇÕES

"""
def mostrarLinha ():
    print('-' *30)


mostrarLinha()
print('FUNÇÕES')
mostrarLinha()
"""

"""
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


mensagem('SISTEMA')
mensagem('TESTE')
"""

"""
def soma(n1, n2):
    s = n1 + n2
    print(f'A soma de {n1} + {n2} é igual a {s}')


soma(2, 3)
soma(int(input('Número: ')), int(input('Segundo número: ')))
"""


"""
def contador(*num):
    print(num)

contador(1,2,6,10)
contador(3,15,6)
"""

"""
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos]*2
        pos += 1

valores = [7, 3, 2, 8]        
dobra(valores)
print(valores)
"""

def soma(*num):
    s = 0
    for n in num:
        s += n
    print(f'A soma dos valores {num} é igual a {s}')

soma(2, 5, 7)
soma(10, 20, 8)