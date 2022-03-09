resp = 'S'
cont = soma = num = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números ea média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'. format(maior, menor))
