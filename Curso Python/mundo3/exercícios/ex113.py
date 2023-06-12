def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO, por favor digite um número inteiro válido.\033[m')
            continue
        else:
            return n
        

def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO, por favor digite um número válido.\033[m')
            continue
        else:
            return n


n = leiaInt('Digite um número: ')