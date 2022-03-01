#Estrutura de repetição while

#exemplo 03:
r = 'S'

while r == 'S':
   n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Fim')

'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('O total de número(s) pare(s) digitados foram {}.'.format(par))
print(('E o total de número(s) ímpare(s) digitados foram {}'.format(impar)))
print('Fim')'''




#exemplo 02:
#n = 1
#while n != 0:
#    n = int(input('Digite um valor: '))
#print('Fim')



# Exemplo 01:
#c = 0
#while c < 10:
#    c = c + 1
#    print(c)
#print('Fim')