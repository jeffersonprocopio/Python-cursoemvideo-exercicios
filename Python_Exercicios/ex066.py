#Programa de Vários números com flag
cont = soma = num = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')