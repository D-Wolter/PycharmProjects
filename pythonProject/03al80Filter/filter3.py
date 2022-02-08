from dados import produtos, pessoas, lista
#filtrar produtos acima de 20 reais

nova_lista = filter(lambda p: p['preco'] > 20, produtos)

for produto in nova_lista:
    print(produto)
    # {'nome': 'p2', 'preco': 55.5}
    # {'nome': 'p4', 'preco': 25}
    # {'nome': 'p5', 'preco': 44.5}
    # {'nome': 'p6', 'preco': 48}
    # {'nome': 'p7', 'preco': 200}
    # {'nome': 'p8', 'preco': 130}
    #