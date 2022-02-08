#retorna que eh menor de idade
from dados import produtos, pessoas, lista

def filtro(pessoa):
    if pessoa['idade'] <= 18:
        return True

nova_lista = filter(filtro, pessoas)


for produto in nova_lista:
    print(produto)
   # {'nome': 'manoel', 'idade': 15}