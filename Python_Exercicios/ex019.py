from random import choice
a = str(input('Primeiro nome: '))
b = str(input('Segundo nome: '))
c = str(input('Terceiro nome: '))
d = str(input('Quarto nome: '))
l = [a, b , c , d]
esc = choice(l)
print('O aluno escolhido foi {}.'.format(esc))