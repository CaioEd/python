# DEFININDO FUNÇÕES

def calcMedia(n1, n2, n3):
    calc = (n1 + n2 + n3)/3
    return calc

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))


print('A média do aluno é: {:.2f}' .format(calcMedia(nota1, nota2, nota3)))