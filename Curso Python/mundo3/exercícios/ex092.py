trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
trabalhador['ano nascimento'] = int(input('Ano de nascimento: '))
trabalhador['idade'] = 2023 - trabalhador['ano nascimento']
trabalhador['carteira trabalho'] = int(input('Carteira de trabalho (0 - não tem): '))

if trabalhador['carteira trabalho'] != 0:
    trabalhador['ano contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = int(input('Salário: '))
    trabalhador['aposentadoria'] = (trabalhador['ano contratação'] + 35) - 2023

    
for k, v in trabalhador.items():
        print(f'{k} é {v}')