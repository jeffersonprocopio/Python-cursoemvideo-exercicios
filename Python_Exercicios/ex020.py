from random import shuffle
a = str(input('Primeiro nome: '))
b = str(input('Segundo nome: '))
c = str(input('Terceiro nome: '))
d = str(input('Quarto nome: '))
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)