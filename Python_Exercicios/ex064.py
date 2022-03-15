#Programa Tratando vários valores
cont = num = soma = 0
num: int = int(input("Digite um número \033[1;31m[999 para parar]:\033[m "))
while num != 999:
    soma += num
    cont += 1
    num: int = int(input("Digite um número \033[1;31m[999 para parar]:\033[m "))
print("Você digitou {} números e a soma entre eles foi {} ".format(cont, soma))