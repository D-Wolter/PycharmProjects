#reduce faz soma de valores( itera cada valor e gera um valor total

from dados import produtos, pessoas, lista
from functools import reduce

#somar todos valores de lista
somar_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
    #     somar     iterar  acumular                    chama lista, a partir de 0
print(somar_lista)
#55