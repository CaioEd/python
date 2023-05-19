# SEQUÊNCIAS ANINHADAS 

notas_sala = [
    [5.5, 7.9, 8.5],
    [9.0, 9.5, 8.5],
    [10.0, 8.0, 5.5]
]

medias = []

for notas_aluno in notas_sala:
    somaNotas = 0
    contaNotas = 0
    for nota in notas_aluno:
        somaNotas += nota
        contaNotas += 1
    media = somaNotas/contaNotas
    medias.append(media)
print(medias)