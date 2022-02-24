real = float(input('Insira um valor para conversão R$'))
dolar = real / 5.46
libra = real / 7.40
euro = real / 6.19
iene = real / 0.048
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar £{:.2f}'. format(real, libra))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥{:.3f}'.format(real, iene))
