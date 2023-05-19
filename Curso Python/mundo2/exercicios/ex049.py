# PROGRAMA QUE FAZ A TABUADA DO NÚMERO QUE O USUÁRIO ESCOLHER

numTab = int(input('Digite o número que você quer saber a tabuada: '))

for c in range(1,11):
    soma = numTab*c
    print('{} X {} = {}' .format(numTab, c, soma))
print('FIM da Tabuada')