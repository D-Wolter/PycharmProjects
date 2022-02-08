from itertools import groupby, tee
alunos = [
    {'nome':'Daniel','nota':'A'},
    {'nome':'luana','nota':'B'},
    {'nome':'tiago','nota':'B'},
    {'nome':'gabriel','nota':'B'},
    {'nome':'joao','nota':'A'},
    {'nome':'andre','nota':'C'},
    {'nome':'manuel','nota':'A'},
    {'nome':'rose','nota':'C'},
    {'nome':'elaine','nota':'B'},
    {'nome':'wilson','nota':'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)#fez uma copia para o iterador for na segunda vez

    print(f' Agrupamento {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
    print()
#  Agrupamento A
# 	{'nome': 'Daniel', 'nota': 'A'}
# 	{'nome': 'joao', 'nota': 'A'}
# 	{'nome': 'manuel', 'nota': 'A'}
# 3 alunos tiraram a nota A
#
#  Agrupamento B
# 	{'nome': 'luana', 'nota': 'B'}
# 	{'nome': 'tiago', 'nota': 'B'}
# 	{'nome': 'gabriel', 'nota': 'B'}
# 	{'nome': 'elaine', 'nota': 'B'}
# 	{'nome': 'wilson', 'nota': 'B'}
# 5 alunos tiraram a nota B
#
#  Agrupamento C
# 	{'nome': 'andre', 'nota': 'C'}
# 	{'nome': 'rose', 'nota': 'C'}
# 2 alunos tiraram a nota C



















