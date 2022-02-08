#criar um dicionario
#d1 = {'chave1' : 'valor da chave'}#as chaves podem ser numero string e tuplas
#d1['nova_chave'] = 'valor da nova chave'#adiciona ao dicionario

#print(d1['chave1'])

dicionario = {
    'str' : 'valor',
    232: 'ouitro valor',
    (1,2,3,4) : 'tupla',
}
#podesse adicionar novas chaves assim
dicionario['naoexiste'] = 'agora existe.'
#ouadicionar assim
dicionario.update({'nova chave' : 'novo valor'})

#podemos apagar uma chave assim
del dicionario['str']
print(dicionario)

#se procura uma chave que nao existe quebra o cod, podese fazer um if
if 'naoexiste' in dicionario:
    print (dicionario['naoexiste'])
print(  dicionario[(1,2,3,4)]  )

print(dicionario['nova chave'])

#ou pode fazer um get que se caso a chave nao existir nao quebra o cod e retorna None
print(dicionario.get('chavequenaoexiste'))

#checar se a chave existe no dicionario retorn True
print(232 in dicionario)
#checar se existe o valor da chave na lista
print('tupla' in dicionario.values())#checa os valores e nao as chaves

#se quiser checar quantas chaves-valor tem usase o len que retorna o numero de chaves
print(len(dicionario))