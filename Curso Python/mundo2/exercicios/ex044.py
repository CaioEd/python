# PROGRAMA CALCULO DE DESCONTOS
# PROGRAMA QUE LE O VALOR GASTO EM UMA LOJA, DEPOIS DA AS OPÇÕES DE PAGAMENTO E CALCULA O VALOR DO DESCONTO DE ACORDO COM A OPÇÃO ESCOLHIDA

preco = float(input('Qual foi o valor da compra ? '))

print('FORMAS DE PAGAMENTO \n [1] à vista dinheiro - 10% desconto \n [2] à vista cartão - 5% desconto \n [3] mais de 1x no cartão - sem desconto \n [4] pix ou boleto - 10% desconto')

opcao = str(input('Qual opção você gostaria de utilizar ? '))

if opcao == '1':
    desc = (preco*10)/100
    precoDesc = preco - desc
    print('Você escolheu dinheiro como forma de pagamento. \n Sua compra passou de R$ {} para R$ {} com 10% de desconto.' .format(preco, precoDesc))
elif opcao == '2':
    desc = (preco*5)/100
    precoDesc = preco - desc
    print('Você escolheu cartão à vista como forma de pagamento. \n Sua compra passou de R$ {} para R$ {} com 5% de desconto.' .format(preco, precoDesc))
elif opcao == '3':
    print('Você escolheu parcelar a compra no cartão. Infelizemnte não temos desconto para essa opção.')
elif opcao == '4':
    desc = (preco*10)/100
    precoDesc = preco - desc
    print('Você escolheu pix ou boleto como forma de pagamento. \n Sua compra passou de R$ {} para R$ {} com 10% de desconto.' .format(preco, precoDesc))
else:
    print('Opção inválida. Por favor tente novamente digitando outra opção.')