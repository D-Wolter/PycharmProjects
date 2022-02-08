 #count contador iterador
from itertools import count
contador = count(start=9)
for valor in contador:
    print(valor)
    if valor >= 19:
        break
        # 9
        # 10
        # 11
        # 12
        # 13
        # 14
        # 15
        # 16
        # 17
        # 18
        # 19
        #