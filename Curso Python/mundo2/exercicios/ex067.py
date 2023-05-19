# PROGRAMA QUE MOSTRA A TABUADA DO NÚMERO DIGITADO PELO USUÁRIO. A SOLICITAÇÃO DO PROGRAMA SÓ SERÁ INTERROMPIDA QUANDO O USUÁRIO DIGITAR UM NÚMERO NEGATIVO.

while True:
    num = 0
    tabNum = int(input('Quer ver a tabuada de qual número ? (Número negativo - Encerrar) '))

    while num < 10 and tabNum > 0:
        num += 1
        print(f'{tabNum} X {num} = {tabNum*num}')

    if tabNum < 0:
        break

print('FIM PROGRAMA')