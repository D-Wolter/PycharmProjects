 #count contador iterador

from itertools import count
contador = count()
print(next(contador))#0
print(next(contador))#1
print(next(contador))#2
print(next(contador))#3
print(next(contador))#4
print(next(contador))#5
print(next(contador))#6
print(next(contador))#7

#contador é um gerador infinito combinado com laco for que sempre puxa a iteracao
for valor in contador:
    print(valor)

    if valor >= 999:
        break