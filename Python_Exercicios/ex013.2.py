#Exemplo salário

salario = float(input('Digite o valor do salário atual R$'))
aumento = float(input('Digite a porcetagem de aumento: '))
desconto = float(input('Digite a porcentagem dos descontos gerais: '))
pda = salario + (salario * aumento / 100)
sf = pda - (pda * desconto /100)

print('O salário atual é o valor de R${:.2f}.'.format(salario))
print('Com o aumento de {}% o salario bruto passará a ser R${:.2f}.'. format(aumento, pda))
print('Com descontos gerais de {}% o salário líquido é de R${:.2f}.'. format(desconto, sf))
