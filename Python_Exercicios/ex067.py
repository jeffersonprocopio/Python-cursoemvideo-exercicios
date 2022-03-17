#Programa de tabuada com while
num = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 50)
    if num <= -1:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-' * 50)
print('-' * 50)
print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
print('-' * 50)

