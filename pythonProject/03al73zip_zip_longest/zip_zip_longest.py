'''
zip - unindo iteraveis

'''

### codigo
cidades = ['sao paulo', 'belo horizonte', 'salvador', 'monte belo']

# codigo
estados = ['sp', 'mg', 'ba']

cidades_estados = zip(cidades, estados)#ele uni as lista mas como tinha tre na segunda ele parou no terceiro
# print(next(cidades_estados))#('sao paulo', 'sp')
# print(next(cidades_estados))#('belo horizonte', 'mg')
# print(next(cidades_estados))#('salvador', 'ba')

#for valor in cidades_estados:
#    print(valor[0], valor[1])
print(list(cidades_estados))#[('sao paulo', 'sp'), ('belo horizonte', 'mg'), ('salvador', 'ba')]
