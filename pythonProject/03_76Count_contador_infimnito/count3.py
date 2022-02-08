 #count contador iterador
from itertools import count
contador = count(start=9, step=2)#comecar a partir do 9 e pular de 2 em 2
for valor in contador:
    print(valor)
    if valor >= 19:
        break
        # 9
        # 11
        # 13
        # 15
        # 17
        # 19
        #