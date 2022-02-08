from itertools import count
contador = count()
lista = ['luis', 'joao', 'maria']
lista = zip(contador, lista)#dessa forma podemos adiciona elementos a lista
print(list(lista))
#[(0, 'luis'), (1, 'joao'), (2, 'maria')]