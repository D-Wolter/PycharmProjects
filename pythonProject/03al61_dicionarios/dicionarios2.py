
dicionario = {
    'chave1' : 'valor',
    'chave2' : 'outro valor',
    'chave3' : 'tupla',
}

#listar chaves do dicionario
for k in dicionario:
    print(k)
    #chave1
    #chave2
    #chave3

#listar valores
for v in dicionario.values():
    print(v)
    #valor
    #outro valor
    #tupla

#listar chave e valor
for kv in dicionario.items():
    print(kv)
    #('chave1', 'valor')
    #('chave2', 'outro valor')
    #('chave3', 'tupla')

#listar chave e valor desempacotado
    print(kv[1], kv[0])
    #valor chave1
    #outro valor chave2
    #tupla chave3
