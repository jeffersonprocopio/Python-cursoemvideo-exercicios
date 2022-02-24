da = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
t = (60 * da) + (0.15 * km)

print('O total a pagar é de R${:.2f}'.format(t))