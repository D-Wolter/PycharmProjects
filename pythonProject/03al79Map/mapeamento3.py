from dados import produtos, pessoas, lista
#lista todas pessoa em pessoas

nomes = map (lambda p: p['nome'], pessoas)# listar os nomes da lista pessoas
idades = map (lambda p: p['idade'], pessoas)# listar as idades da lista pessoas

for pessoa in pessoas:#listar cada item da lista pessoa
    print(pessoa)

for pessoa in nomes:#listar cada nome da lista pessoas
    print(pessoa)

for pessoa in idades:#listar por idade
    print(pessoa)
# {'nome': 'daniel', 'idade': 40}
# {'nome': 'luana', 'idade': 55}
# {'nome': 'tiago', 'idade': 53}
# {'nome': 'gabriel', 'idade': 25}
# {'nome': 'francvisco', 'idade': 32}
# {'nome': 'renato', 'idade': 34}
# {'nome': 'joao', 'idade': 55}
# {'nome': 'manoel', 'idade': 15}
# {'nome': 'maria', 'idade': 50}
# {'nome': 'roberta', 'idade': 40}
# daniel
# luana
# tiago
# gabriel
# francvisco
# renato
# joao
# manoel
# maria
# roberta
# 40
# 55
# 53
# 25
# 32
# 34
# 55
# 15
# 50
# 40

