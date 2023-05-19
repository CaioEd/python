# MOSTRE QUANTAS VEZES A LETRA "A" APARECE NA FRASE, A PRIMEIRA VEZ QUE APARECEU E A ÚLTIMA VEZ QUE APARECEU

frase = str(input('Digite uma frase:')).lower()
fraseA = frase.count('a', 0)

print('A letra A apareceu {} vezes na frase' .format(fraseA))
