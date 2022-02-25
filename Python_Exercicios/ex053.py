#Programa de Detector de Palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O invervo de {} é {}'.format(junto, inverso))
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# segundo opção de resolver o exercicio

#inverso = ''
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]