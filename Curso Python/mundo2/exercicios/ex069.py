# PROGRAMA QUE LÊ NOME, IDADE E SEXO DAS PESSOAS. A CADA PESSOA CADASTRADA O PROGRAMA DEVEREÁ PERGUNTAR SE A PESSOA QUER CONTINUAR OU NÃO. NO FINAL DEVERÁ MOSTRAR - QUANTAS PESSOAS TEM MAIS DE 18 ANOS, QUANTOS HOMENS FORAM CADASTRADOS E QUANTAS MULHERES TEM MENOS DE 20 ANOS.

maior18 = 0
homens = 0
mMenos20 = 0

while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:')).strip().upper()[0]

    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if idade >= 18:
        maior18 =  maior18+1

    if sexo == 'M':
        homens = homens+1

    if idade < 20 and sexo == 'F':
        mMenos20 = mMenos20+1

    if continuar == 'N':
        break
        

print(f'No total foram cadastradas {maior18} pessoas maiores de idade \n {homens} homens e \n {mMenos20} mulheres com menos de 20 anos')
print('FIM')