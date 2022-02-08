lista = [10,51,62,543,84,35]
lista = iter(lista)#funcao torna a lista auto interavel

print(next(lista))#10
print(next(lista))#51
print(next(lista))#62
print(next(lista))#543
print(next(lista))#84
print(next(lista))#35

print(hasattr(lista, '__next__'))#True