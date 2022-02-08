variavel = ['daniel', 'Wolter', "martins"]

palavra_c_W = False#indica ser false
for valor in variavel:
    if valor.startswith('W'):#como existe o W
        palavra_c_W = True#converte em true

if palavra_c_W:# como virou true executa aqui
    print('existe')
else:
    print('nao')