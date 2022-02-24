# Programa que verifica qual valor é maior ou menor
n1 = int(input('Primerio valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n3:
    menor = n3
print('O menor valor digitado foi {}'.format(menor))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))

# OU
# menor = n1
# if n2 < menor:
#    menor = n2
# if n3 < menor:
#    menor = n3
# print('O menor valor digitado foi {}'.format(menor))
# maior = n1
# if  n2 > maior:
#    maior = n2
# if n3 > maior:
#    maior = n3
# print('O maior valor digitado foi {}'.format(maior))
