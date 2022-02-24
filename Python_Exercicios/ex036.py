#programa que verifica um emprestimo para compra de uma casa
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
a = (salario * 30 / 100)
print('Para pagar um casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= a:
    print('Empréstimo pode ser\033[1;33m CONCEDIDO!\033[m')
else:
    print('Empréstimo\033[1;31m NEGADO!\033[m')
