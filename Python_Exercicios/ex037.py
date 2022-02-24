#Programa de converter numero para Binário, Octal e Hexadecimal
valor = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão: 
[ 1 ] converter para \033[1;32mBINÁRIO\033[m
[ 2 ] converter para \033[1;31mOCTAL\033[m
[ 3 ] converter para \033[1;33mHEXADECIMAL\033[m''')

op = int(input('Sua opção: '))

if op == 1:
    print('{} covertido para \033[1;32mBINÁRIO\033[m é igual a {}'.format(valor, bin(valor)[2:]))
elif op == 2:
    print('{} covertido para \033[1;32mOCTAL\033[m é igual a {}'.format(valor, oct(valor)[2:]))
elif op == 3:
    print('{} covertido para \033[1;32mHEXADECIMA\033[m é igual a {}'.format(valor, hex(valor)[2:]))
else:
    print('Opção inválida, digite uma opção entre 1 a 4')
