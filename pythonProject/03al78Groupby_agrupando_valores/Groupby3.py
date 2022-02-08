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
    for aluno in valores_agrupados:
        print(aluno)
    print()
#         Agrupamento A
#         A
#     {'nome': 'Daniel', 'nota': 'A'}
#     {'nome': 'joao', 'nota': 'A'}
#     {'nome': 'manuel', 'nota': 'A'}

#     Agrupamento b
#
# {'nome': 'luana', 'nota': 'B'}
# {'nome': 'tiago', 'nota': 'B'}
# {'nome': 'gabriel', 'nota': 'B'}
# {'nome': 'elaine', 'nota': 'B'}
# {'nome': 'wilson', 'nota': 'B'}

# Agrupamento c
# C
# {'nome': 'andre', 'nota': 'C'}
# {'nome': 'rose', 'nota': 'C'}
