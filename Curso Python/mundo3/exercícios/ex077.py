# PROGRAMA QUE TEM UMA TUPLA COM VÁRIAS PALAVRAS. MOSTRA PARA CADA PALAVA SUAS VOGAIS

palavras = ('Aprender',
'Maça',
'Controle',          
'Mãe', 
'Ler'           
)



for palavra in palavras:
    print(f'As vogais de {palavra} são: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra)