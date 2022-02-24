#Programa de Progresão aritimetica

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
v = n1 + (10 - 1) * n2
for c in range(n1, v + n2, n2):
    print('{} '.format(c), end='→ ')

print('\033[1;33mAcabou\033[m')