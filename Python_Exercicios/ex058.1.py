#Programa feito para o programa advinhar um numero 2.1
from random import randint
computador = randint(0, 10)
print('''Sou seu computador ...
Acabei de pensar em um número entre 0 e 10. 
Será que você consegue advinhar qual foi? ''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou == True
    else:
        if jogador < computador:
            print('Maiss... Tente mais um vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acerou com {} tentativas. Parabéns'.format(palpites))