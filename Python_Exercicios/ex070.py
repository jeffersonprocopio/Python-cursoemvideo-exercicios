print("--"*20)
print('          LOJA SUPER BARATÃO')
print("--"*20)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    resp = ' '
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'O total de produtos acima de R$1000,00 é {totmil}')
print(f'O produto mais barato  foi {barato} que custa R${menor:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))
