def leiaInt(txt):
    txt = str(input(txt))
   
    while True:
        if txt.isnumeric():
            return txt
            break
        else:
            erro = str(input('Digite apenas números: '))
            if erro.isnumeric():
                break



n = leiaInt('Digite um número: ')