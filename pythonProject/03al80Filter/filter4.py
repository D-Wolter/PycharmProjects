#filtrar produtos acima de 50 reais
#cod igual o de antes mais com funcao que pode ser reaproveitadas em outros processos

from dados import produtos, pessoas, lista

def filtro(produto):
    if produto['preco'] > 50:
        return True

nova_lista = filter(filtro, produtos)


for produto in nova_lista:
    print(produto)
# {'nome': 'p2', 'preco': 55.5}
# {'nome': 'p7', 'preco': 200}
# {'nome': 'p8', 'preco': 130}
