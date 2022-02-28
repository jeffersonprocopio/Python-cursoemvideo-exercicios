n1 = float(input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Voce está aprovado!')
else:
    print('Você está reprovado.')


#Exemplo 01
#nome = str(input('Qual é o seu nome? ')).strip()
#if nome == 'Gustavo':
    #print('Que nome feio você tem em!')
#else:
    #print('Seu nome é bonito!')
#print('Bom dia {}!'.format(nome))