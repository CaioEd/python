# PROGRAMA QUE MOSTRA A CONTAGEM REGRESSIVA PARA O ANO NOVO, INDO DE 10 A 0 COM UMA PAUSA DE 1 SEGUNDO.

import time

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print('Feliz Ano Novo!')