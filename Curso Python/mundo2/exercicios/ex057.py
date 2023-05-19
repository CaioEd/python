# PROGRAMA QUE LE O SEXO DE UMA PESSOA, MAS SÓ ACEITA OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0] # UPPER[0] PEGA SÓ A PRIMEIRA LETRA E STRIP ELIMINA OS ESPAÇOS

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Informe seu sexo novamente: [M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso!' .format(sexo))
