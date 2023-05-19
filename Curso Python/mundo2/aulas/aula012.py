# CONDIÇÕES ANINHADAS

# DESAFIO 040
# APROVADO, REPROVADO, RECUPRAÇÃO

nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
trabalho = float(input('Digite a nota do seu trabalho:'))

media = (nota1+nota2+trabalho)/3

if media <= 4.9:
    print('Sua média foi {:.1f}, você foi REPROVADO!' .format(media))
elif media >=5.0 and media <= 5.9:
    print('Sua média foi {:.1f}, você está de RECUPERAÇÃO' .format(media))
elif media >=6.0 and media <=10.0:
    print('Sua média foi {:.1f}. Parabéns você está APROVADO!' .format(media))
if media < 0 or media > 10.0:
    print('Você digitou um valor inválido. Por favor preencha os dados novamente.')