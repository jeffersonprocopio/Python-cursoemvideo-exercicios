#Programa de Progresão aritimetica 3.0
print('\033[1;32mGerador de PA\033[m')
print('\033[1;32m-=\033[m' *10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('\033[1;33mPAUSA\033[m')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('\033[1;33mProgressão finalizada com {} termos mostrados\033[m'.format(total))
