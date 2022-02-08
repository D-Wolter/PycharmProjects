
clienteslist = {
    'clientevip' : {
        'nome' : 'daniel',
        'sobrenome' : 'wolter',
    },
    'clientes' : {
        'nome' : ' Joao',
        "sobrenome" : 'moreira',
    },
}


for clientes_k, cliente_v in clienteslist.items():#laço for exibe apenas as chaves tipo de cliente
    print(f' exibindo {clientes_k}')
    # exibindo clientevip
    #exibindo clientes
    for dados_k,dados_v in cliente_v.items():#laço verifica o valor dentro das chaves
        print(f'\t{dados_k} = {dados_v}')#\t foi para exibir com 4 espaços antes no print
        #exibindo clientevip
        #    nome = daniel
        #    sobrenome = wolter
        #exibindo clientes
        #    nome =  Joao
        #    sobrenome = moreira

