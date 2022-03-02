#Proma que Cria um Menu de Opções
from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Reiniciar
    [ 5 ] Sair do programa''')
    op = int(input('>>>>> Qual é sua opção? '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif op == 2:
        multi = n1 * n2
        print('O resultado  entre {} x {} é {}'.format(n1, n2,multi))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
    print('=-='*10)
print('Fim do programa! Volte sempre!!')


