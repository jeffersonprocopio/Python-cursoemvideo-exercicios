C = float(input('Informe a temperatura em °C: '))
F = (C * 1.8) + 32 #ou ((9 *C ) /5) + 32 ou 9 * C /5 + 32
K = (C + 273.15)
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F.'. format(C, F))
print('A temperatura de {:.1f}°C corresponde a {:.2f}K.'. format(C, K))