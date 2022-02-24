#PROGRAMA QUE VERIFICA QUANTO TEMPO PARA O ALISTAMENTO
from datetime import date
atual = date.today().year
nome = str(input('Qual seu nome completo: ')).upper().strip()
gen = str(input('Você é do gênero masculino ou feminino: ')).upper().strip()
ano = int(input('Ano de nascimento: '))
id = atual - ano
print('{} do gênero {} nasceu em {} tem {} ano(s) no ano {}'.format(nome, gen, ano, id, atual,))
if gen == 'FEMININO':
    print('Pessoas do gênero feminino não precisam se alistarem')
elif id < 18:
    n1 = 18 - id
    n2 = n1 + atual
    print('Ainda faltam {} ano(s) para o alistamento'.format(n1))
    print('Seu alistamento será em {}.'.format(n2))
elif id > 18:
    n3 = id - 18
    n4 = atual - n3
    print('Você ja deveria ter se alistado há {} ano(s)'.format(n3))
    print('Seu alistamento foi em {}.'.format(n4))

elif id == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
