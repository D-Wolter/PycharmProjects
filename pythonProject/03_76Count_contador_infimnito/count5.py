from itertools import count
contador = count(start=9, step=-1)
for valor in contador:
    print(round(valor, 2))#round areddonda valor 2 determina a quantidade de casas decimais
    if valor >= 10 or valor <= -10:
        break
        # 9
        # 8
        # 7
        # 6
        # 5
        # 4
        # 3
        # 2
        # 1
        # 0
        # -1
        # -2
        # -3
        # -4
        # -5
        # -6
        # -7
        # -8
        # -9
        # -10
        # 