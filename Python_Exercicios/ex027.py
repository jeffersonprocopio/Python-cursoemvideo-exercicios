nome = str(input('Digite seu nome completo: ')).strip()
pn = nome.split()
print('Muito prazer em te conhecer {}!!!'.format(nome))
print('Seu primeiro nome é {}.'.format(pn[0]))
print('Seu último nome é {}.'.format(pn[len(pn)-1]))


