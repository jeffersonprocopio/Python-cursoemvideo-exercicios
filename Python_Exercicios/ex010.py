#Conversor de moeda
real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.46
print('Com R${:.2f} você pode comprar US${:.2f}'. format(real, dolar))

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
euro = real / 6.19
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
libra = real / 7.40
print('Com R${:.2f} você pode comprar £{:.2f}'.format(real, libra))