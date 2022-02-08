

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(["joao", 'maria', 'jose'])
clientes2 = lista_de_clientes(["dani", 'tiago', 'luana'])

print(clientes1)
print(clientes2)