'''
Itertolls
Combinations - ordem nao importa, nao repetem valores unico
permutations - ordem importa, nao repetem valores unico
Product - Ordem importa e repete valores unicos
'''

from itertools import combinations
pessoas = ['daniel', 'tiago', 'elaine','wilson','luana','gabriel']
for grupo_d_2 in combinations(pessoas, 2):
    print(grupo_d_2)
    # ('daniel', 'tiago')
    # ('daniel', 'elaine')
    # ('daniel', 'wilson')
    # ('daniel', 'luana')
    # ('daniel', 'gabriel')
    # ('tiago', 'elaine')
    # ('tiago', 'wilson')
    # ('tiago', 'luana')
    # ('tiago', 'gabriel')
    # ('elaine', 'wilson')
    # ('elaine', 'luana')
    # ('elaine', 'gabriel')
    # ('wilson', 'luana')
    # ('wilson', 'gabriel')
    # ('luana', 'gabriel')
    #

