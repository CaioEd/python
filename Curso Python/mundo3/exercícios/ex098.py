from time import sleep

def mostrarLinha():
    print('-='*30)

def contador(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(c)
        sleep(0.5)
    c += 1


print('Contagem de 1 até 10, de 1 em 1')
mostrarLinha()

contador(1, 11, 1)

mostrarLinha()
print('contagem de 10 até 0, de 2 em 2')
mostrarLinha()

contador(10, -1, -2)

mostrarLinha()
print('Contagem personalizada: ')
ini = int(input('Início contagem: '))
f = int(input('Fim da contagem (+1): '))
pas = int(input('Passo: '))

contador(ini, f, pas)