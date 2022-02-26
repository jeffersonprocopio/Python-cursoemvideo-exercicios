#Programa que verifica qual quem tem o maior e o menor peso
maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.2f}Kg'.format(maior))
print('O manor peso lido foi de {:.2f}Kg'.format(menor))
