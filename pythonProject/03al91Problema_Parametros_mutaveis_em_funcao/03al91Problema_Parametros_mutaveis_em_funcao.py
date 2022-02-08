#mutavel: listas, dicionarios
#imutavel: tuplas, strings, numeros, true, false, none.

#forma erraDA
def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(["joao", 'maria', 'jose'])
clientes2 = lista_de_clientes(["dani", 'tiago', 'luana'])

print(clientes1)
print(clientes2)
# ['joao', 'maria', 'jose', 'dani', 'tiago', 'luana']
# ['joao', 'maria', 'jose', 'dani', 'tiago', 'luana']
