#Programa feito para o programa advinhar um numero 2.0
from random import randint

computador = randint(0, 10)
tot = 0

print('''Sou seu computador ...
Acabei de pensar em um número entre 0 e 10. 
Será que você consegue advinhar qual foi? ''')

n = int(input('Em que número eu pensei? '))# Jogador tenta advinhar

while n != computador:
    print('Tente outra vez, você não advinhou HAHA!')
    n = int(input('Em que número eu pensei? '))
    tot += 1
print('Você acertou com {} tentativas. PARABÉNS! você, conseguiu me vencer!!'.format(tot))
print(computador)