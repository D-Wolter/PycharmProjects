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

#alunos.sort(key=lambda item: item['nota'])# funcao lambda ordena por nota
#print(alunos)
#[{'nome': 'Daniel', 'nota': 'A'}, {'nome': 'joao', 'nota': 'A'}, {'nome': 'manuel', 'nota': 'A'}, {'nome': 'luana', 'nota': 'B'}, {'nome': 'tiago', 'nota': 'B'}, {'nome': 'gabriel', 'nota': 'B'}, {'nome': 'elaine', 'nota': 'B'}, {'nome': 'wilson', 'nota': 'B'}, {'nome': 'andre', 'nota': 'C'}, {'nome': 'rose', 'nota': 'C'}]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)# criou trez grupos os de a b c

for grupos in alunos_agrupados:
    print(grupos)
    # ('A', < itertools._grouper object at 0x000000F177059F70 >)
    # ('B', < itertools._grouper object at 0x000000F177059F40 >)
    # ('C', < itertools._grouper object at 0x000000F177059F70 >)
    #