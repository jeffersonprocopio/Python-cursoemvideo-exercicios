nome = str(input('Digite seu nome completo: '))

pn = nome.split()

print('Analisando seu nome....')
print('O seu nome com letra maiúculas fica {}.'.format(nome.upper()))
print('O seu nome com letra maiúculas fica {}.'.format(nome.lower()))
print('O seu nome ao total tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(pn[0], len(pn[0])))



#nome = str(input('Digite seu nome completo: ')).strip()

#pn = nome.split()

#print('Analisando seu nome...')
#print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
#print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
#print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(n,nome.find(' ')))
#print('Seu primeiro nome é {} e ele tem {} letras'.format(pn[0], len(pn[0])))