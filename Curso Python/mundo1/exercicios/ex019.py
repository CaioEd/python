# SORTEIO DOS ALUNOS

import random

alunos = [input('Primeiro aluno:'), input('Segundo aluno:'), input('Terceiro aluno:')]


print('O aluno sorteado foi {}' .format(random.choices(alunos)))
