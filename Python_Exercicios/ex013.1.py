#Exemplos de desconto e aumento por porcentagem

produto = float(input('Qual é o valor do produto? R$'))
desconto = float(input('Qual é a porcentagem do desconto para pagamento a vista: '))
juros = float(input('Qual é a pórcentagem de aumento para pagamentos parcelados: '))
pd = produto - (produto * desconto / 100)
pj = produto + (produto * juros / 100)

print('O valor do produto é R${:.2f}.'.format(produto))
print('A porcentagem de desconto para pagamento a vista é de {}%'.format(desconto))
print('A porcentagem de aumento para parcelamento é de {}%'.format(juros))
print('O valor do produto com pagamento a vista é R${:.2f} e o valor final parcelado fica R${:.2f}'.format(pd, pj))

