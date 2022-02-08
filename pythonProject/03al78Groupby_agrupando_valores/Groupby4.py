from itertools import groupby
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
    print(f' Agrupamento {agrupamento}')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
# Agrupamento A
# 3 alunos tiraram a nota A
# Agrupamento B
# 5 alunos tiraram a nota B
# Agrupamento C
# 2 alunos tiraram a nota C
