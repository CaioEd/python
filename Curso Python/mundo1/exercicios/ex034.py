# AUMENTO DE SALÁRIOS

nome = str(input('Digite o nome do funcionário:'))
salario = int(input('Digite o salário do funcionário:'))

salarioNovo15 = salario + ( (15*salario)/100 ) 
salarioNovo10 = salario + ((10*salario)/100) 

if salario <= 1250:
    print('{} teve um aumento de 15% no salário. Passou a ganhar R$ {}' .format(nome, salarioNovo15))
else:
    print('{} teve um aumento de 10% no salário. Passou a ganhar R$ {}' .format(nome, salarioNovo10))