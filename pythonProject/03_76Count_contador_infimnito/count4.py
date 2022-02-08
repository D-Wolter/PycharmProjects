from itertools import count
contador = count(start=5, step=0.05)
for valor in contador:
    print(round(valor, 2))#round areddonda valor 2 determina a quantidade de casas decimais
    if valor >= 19:
        break