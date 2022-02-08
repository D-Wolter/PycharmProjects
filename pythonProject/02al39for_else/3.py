variavel = ['daniel', 'Wolter', "martins"]

palavra_c_W = False#indica ser false
for valor in variavel:
    if valor.lower().startswith('w'):#.lower tranforma em minusculo, startswith verifica se a primira letra da variavel eh minuscula
        palavra_c_W = True#converte em true

if palavra_c_W:# como virou true executa aqui
    print('existe')
else:
    print('nao')