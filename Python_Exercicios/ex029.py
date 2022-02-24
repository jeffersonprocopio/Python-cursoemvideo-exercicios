#Programa de gerar multa caso ultrapassar a velocidade
v = float(input('Qual a velocidade atual do carro? '))
multa = (v - 80) * 7
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança! Use sinto de sergurança!')

#ou
#else:
    #print('Tenha um bom dia! Dirija com segurança! Use sinto de sergurança!')




#2° metodo de fazer
#v = float(input('Qual a velovidade atual do carro? '))
#r = (80)
#m = (v - 80) * 7
#if v <= r:
#    print('Tenha um bom dia! Dirija com segurança! Use sinto de sergurança!')
#else:
#    print('MULTADO! Você excedeu o limite de permitido que é de 80Km/h')
#    print('Você deve pagar uma multa de R${:.2f}'.format(m))
#    print('Tenha um bom dia! Dirija com segurança! Use sinto de sergurança!')