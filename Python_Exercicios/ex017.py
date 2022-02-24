#import math
import math
from math import hypot
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co** 2 + ca** 2)
#r = math.sqrt(hi)
#print('A hipotenusa vai medir {:.2f}'.format(r))

#Outros exemplos de como calcular a hipotenusa

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto  adjacente: '))
#hi = (co ** 2 + ca ** 2 ) ** (1/2)
#print(' A hipotesusa vai medir {:.2f}'. format(hi))

#from math import hypot
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto  adjacente: '))
#hi = hypot(ca,co)
#print ('A hipotenusa vai medir {:.2f}'.format(hi))

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto  adjacente: '))
hi = math.hypot(ca,co)

print ('A hipotenusa vai medir {:.2f}'.format(hi))