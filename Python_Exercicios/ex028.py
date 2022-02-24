#Programa feito para o programar advinhar um numero
from random import randint
from time import sleep #Biblioteca que fazer esperar para o programa
computador = randint (0, 5) #Faz o computador escolher um número aletório
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))# Jogador tenta advinhar
print('PROCESSANDO....')
sleep(3)
if n == computador:
    print('PARABÉNS! Você, conseguiu me vencer!!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, n))
