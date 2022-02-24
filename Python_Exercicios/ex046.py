#programa de contagem regressiva
import emoji
from time import sleep
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
print(emoji.emojize("\033[1;33mBUM! BUM! POOOW!\033[m \033[1;31m:fireworks:\033[m ", use_aliases=True))