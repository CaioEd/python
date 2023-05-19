# PROGRAMA QUE LE DOIS NÚMEROS E DA OPÇÕES DE SOMAR, SUBTRAIR, DIGITAR NOVOS VALORES OU SAIR DO PROGRAMA.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print('[1] somar \n [2] subtrair \n [3] novos números \n [4] sair do programa')

opcao = str(input('Qual opção você escolhe ?'))


while opcao not in '4':

    if opcao == '1':
        res = num1+num2
        print('Resultado: {}' .format(res))
    elif opcao == '2':
        res = num1-num2
    elif opcao == '3':
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print('[1] somar \n [2] subtrair')
        opcao = str(input('Qual opção você escolhe ?'))
        if opcao == '1':
            res = num1+num2
            print('Resultado: {}' .format(res))
        elif opcao == '2':
            res = num1-num2
            print('Resultado: {}' .format(res))

    print('Resultado: {}' .format(res))
    print('[1] somar \n [2] subtrair \n [3] novos números \n [4] sair do programa')

    opcao = str(input('Qual opção você escolhe ?'))
print('====== FIM ======')