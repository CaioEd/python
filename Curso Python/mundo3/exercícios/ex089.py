lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar ? [S/N]'))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    notas = int(input('Digite o número do aluno que você deseja ver as notas [999-interromper]: '))

    if notas == 999:
        break
    elif notas <= len(lista) -1:
        print(f'Aluno {[lista[notas][0]]} \n Notas: {lista[notas][1]}')
