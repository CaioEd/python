# ORDEM DE APRESENTAÇÃO

import random

listaAlunos = [input('Primeiro aluno:'), input('Segundo aluno:'), input('Terceiro aluno:')]
random.shuffle(listaAlunos)

print('A ordem de apresentação será \n {}' .format(listaAlunos))