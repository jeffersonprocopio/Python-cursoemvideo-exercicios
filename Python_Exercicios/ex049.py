#Tabuada usando for. vol 2
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))


#ou
#for c in range (0, 10):
#    n1 = n1 + 1
#    n2 = n2 + 1 * num
#    print('{} x {:2} = {}'.format(num, n1, n2))