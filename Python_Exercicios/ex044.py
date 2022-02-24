print('\033[1;33m{:=^50}\033[m'.format('\033[1;33m LOJAS PROCÓPIO '))

preço = float(input('Preço das compras: R$'))

print('\033[1mFORMAS DE PAGAMENTO\033[m')
print('[ 1 ] á vista dinheiro/pix/cheque.')
print('[ 2 ] á vista no cartão.')
print('[ 3 ] 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão.')
op = int(input('Qual sua opção? '))

if op == 1:
    des = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, des))
elif op == 2:
    des = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, des))
elif op == 3:
    parcela = int(input('Quantas parcelas? '))
    norm = preço / parcela
    print('Sua compra será parcelada {}x de R${:.2f} SEM JUROS'.format(parcela, norm))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, preço))
elif op == 4:
    parcela = int(input('Quantas parcelas? '))
    j1 = preço + (preço * 20 / 100)
    j2 = j1 /parcela
    print('Sua compra será parcelada {}x de R${:.2f} COM JUROS'.format(parcela, j2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, j1))
else:
    print('Opção inválida, digite uma opção entre 1 a 4')