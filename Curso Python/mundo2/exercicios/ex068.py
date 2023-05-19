# JOGO PAR OU ÍMPAR - PROGRAMA QUE PODEMOS JOGAR PAR OU ÍMPAR COM O COMPUTADOR. O PROGRAMA IRÁ SOLICITAR UM VALOR AO USUÁRIO E 'PENSARA UM UM NÚMERO ALEATÓRIO'. O PROGRAMA TAMBÉM IRÁ PEDIR PRO USUÁRIO ESCOLHER ENTRE PAR OU ÍMPAR. O JOGO SÓ SERÁ ENCERRADO QUANDO O USUÁRIO PERDER E MOSTRARA A QUANTIDADE DE VITÓRIAS DELE.

import random

print('=========================')
print('Vamos jogar par ou ímpar!')
print('=========================')

contVit = 0

while True:

    numProg = random.randint(1, 10)
    numUsu = int(input('Diga um valor entre 1 e 10: '))

    parImp = str(input('Par ou Ímpar: [P/I] ')).strip().upper()[0]

    total = numProg + numUsu

    print('-----')

    if total%2 == 0:
        print(f'Você jogou {numUsu} e o computador {numProg}, no total deu {total} que é PAR!')
        print('-----')

        if  parImp == 'P':
            print('Você venceu!')
            contVit += 1
        elif parImp == 'I':
            print(f'Você perdeu \n ganhou {contVit} vezes!')
            break

    if total%2 != 0:
        print(f'Você jogou {numUsu} e o computador {numProg}, no total deu {total} que é ÍMPAR!')
        print('-----')

        if  parImp == 'I':
            print('Você venceu!')
            contVit += 1
        elif parImp == 'P':
            print(f'Você perdeu \n ganhou {contVit} vezes!')
            break
            


