#como ordenar por nota com groupby

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

alunos.sort(key=lambda item: item['nota'])# funcao lambda ordena por nota
#print(alunos)
#[{'nome': 'Daniel', 'nota': 'A'}, {'nome': 'joao', 'nota': 'A'}, {'nome': 'manuel', 'nota': 'A'}, {'nome': 'luana', 'nota': 'B'}, {'nome': 'tiago', 'nota': 'B'}, {'nome': 'gabriel', 'nota': 'B'}, {'nome': 'elaine', 'nota': 'B'}, {'nome': 'wilson', 'nota': 'B'}, {'nome': 'andre', 'nota': 'C'}, {'nome': 'rose', 'nota': 'C'}]

for aluno in alunos:
    print(aluno)
    # {'nome': 'Daniel', 'nota': 'A'}
    # {'nome': 'joao', 'nota': 'A'}
    # {'nome': 'manuel', 'nota': 'A'}
    # {'nome': 'luana', 'nota': 'B'}
    # {'nome': 'tiago', 'nota': 'B'}
    # {'nome': 'gabriel', 'nota': 'B'}
    # {'nome': 'elaine', 'nota': 'B'}
    # {'nome': 'wilson', 'nota': 'B'}
    # {'nome': 'andre', 'nota': 'C'}
    # {'nome': 'rose', 'nota': 'C'}