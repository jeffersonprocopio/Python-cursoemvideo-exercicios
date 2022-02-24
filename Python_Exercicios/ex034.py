#Programa de aumento de salario
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    s15 = salario + (salario * 15 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, s15))
else:
    s10 = salario + (salario * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, s10))