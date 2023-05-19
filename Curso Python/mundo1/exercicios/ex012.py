#  DESCONTO PRODUTOS

produto = str(input('Digite o nome do produto:'))
precoProduto = float(input('Digite o preço do produto e descubra quanto fica com 5% de desconto:'))

valorDesconto = (5*precoProduto)/100
valornovo = precoProduto - valorDesconto

print('O valor do(a) {} com nosso cupom de 5% de desconto é: {:.2f}' .format(produto, valornovo))