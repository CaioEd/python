from datetime import date

def voto(anoNasc):
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if idade >= 18 and idade <= 65:
        return ('VOTO OBRIGATÓRIO!')
    elif idade >= 16 and idade <= 17 or idade > 65:
        return ('VOTO OPCIONAL!')
    else:
        return ('VOTO NEGADO!')
    

anoNascimento = int(input('Informe seu ano de nascimento: '))

print(voto(anoNascimento))