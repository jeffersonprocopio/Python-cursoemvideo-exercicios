n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
#print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'. format(n, (n*2), n, (n*3), n, (n**(1/2)))) ou pow
print('O dobro de {} vale {}'. format(n, d))
print('O triplo de {} vale {}'. format(n, t))
print('A raiz quadrada de {} é igual a {:.2f}'.format(n, r))