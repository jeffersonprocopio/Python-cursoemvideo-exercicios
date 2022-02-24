#Programa que classifa conforme a idade
from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento: '))
id = atual - ano

print('O(a) atleta tem {} ano(s)'.format(id))

if id <= 9:
    print('Ele(a) classifica na categoria: \033[1;31mMIRIM\033[m')
elif id <= 14:
    print('Ele(a) se classifica na categoria: \033[1;32mINFANTIL\033[m')
elif id <= 19:
    print('Ele(a) se classfica na categoria: \033[1;33mJÚNIOR\033[m')
elif id <= 25:
    print('Ele(a) se classfica na categoria: \033[1;34mSÊNIOR\033[m')
elif id > 25:
    print('Ele(a) se classfica na categoria: \033[1;35mMASTER\033[m')
