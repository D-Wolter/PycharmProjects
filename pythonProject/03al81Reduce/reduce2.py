#reduce faz soma de valores( itera cada valor e gera um valor total

from dados import produtos, pessoas, lista
from functools import reduce

#somar todos valores de produtos
soma_precos = reduce(lambda acumulador, preco: preco['preco'] + acumulador, produtos, 0)
print(soma_precos)
#537.4