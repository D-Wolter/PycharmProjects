'''
Itertolls
Combinations - ordem nao importa, nao repetem valores unico
permutations - ordem importa, nao repetem valores unico
Product - Ordem importa e repete valores unicos
'''
#Combinations - ordem nao importa, nao repetem valores unico
#se holver um par como Luana e Gabriel, nao repete Gabriel e luana (para repetir chama Permutations)
#product mostra pares repetidos como no permutations e tambem pares do mesmo nome luana e luana.

from itertools import permutations
pessoas = ['daniel', 'tiago', 'elaine','wilson','luana','gabriel']
for grupo_d_2 in permutations(pessoas, 2):#comando do numero de grupos 2
    print(grupo_d_2)
    # ('daniel', 'tiago')
    # ('daniel', 'elaine')
    # ('daniel', 'wilson')
    # ('daniel', 'luana')
    # ('daniel', 'gabriel')
    # ('tiago', 'daniel')
    # ('tiago', 'elaine')
    # ('tiago', 'wilson')
    # ('tiago', 'luana')
    # ('tiago', 'gabriel')
    # ('elaine', 'daniel')
    # ('elaine', 'tiago')
    # ('elaine', 'wilson')
    # ('elaine', 'luana')
    # ('elaine', 'gabriel')
    # ('wilson', 'daniel')
    # ('wilson', 'tiago')
    # ('wilson', 'elaine')
    # ('wilson', 'luana')
    # ('wilson', 'gabriel')
    # ('luana', 'daniel')
    # ('luana', 'tiago')
    # ('luana', 'elaine')
    # ('luana', 'wilson')
    # ('luana', 'gabriel')
    # ('gabriel', 'daniel')
    # ('gabriel', 'tiago')
    # ('gabriel', 'elaine')
    # ('gabriel', 'wilson')
    # ('gabriel', 'luana')
    #
