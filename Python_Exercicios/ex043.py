#PROGRAMA QUE VERIFICA O IMC
peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.2f}.'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!!')
elif imc < 25:
    print('PA RABÉNS, você está na faixa de PESO NORMAL')
elif imc < 30:
    print('ATENÇÃO, você está na faixa de SOBREPESO!')
elif imc < 40:
    print('CUIDADO, você está na faixa de OBSESIDADE!')
else:
    print('CUIDE SE, você está na faixa de OBESIDADE MÓRBIDA!!!')