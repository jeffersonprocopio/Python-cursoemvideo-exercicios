print("--"*20)
print("CADASTRE UMA PESSOAS")
print("--"*20)
tot18 = totM = totF20 = totF= totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F':
        totF += 1
    if sexo == 'F' and idade < 20:
         totF20 += 1
    if sexo == 'M' and idade < 20:
         totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas acima de 18 anos: {tot18}')
print(f'Ao todo temos {totM} homens cadastrados')
print(f'Ao todo temos {totF} mulheres cadastradas')
print(f'Total de mulheres com 20 anos: {totF20}')
print(f'Total de homens com 20 anos: {totM20}')

