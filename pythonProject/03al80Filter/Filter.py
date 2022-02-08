from dados import produtos, pessoas, lista
# diferentre de map, filter retorna true or false

nova_lista = filter(lambda x: x > 5, lista)#chama fumcao filter, primeiro argumento funcao lambda
# lambda ve todos os valores da lista maior que 5, chama a lista no fim

print(nova_lista)#filter retorna um iterator dai fazemos um cast para lista
print(list(nova_lista))
# <filter object at 0x000000D11D919400>
# [6, 7, 8, 9, 10]
