#forma de somar comprar de carrinho virtual

carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', '20'))
carrinho.append(('Produto 3', 50))

#no python essa baixo nao eh muito boa
# total = []
# for produto in carrinho:
#     total.append(produto[1])
# print(sum(total))

total = sum([float(y) for x, y in carrinho])#sum soma float y #jeito certo de fazer soma
#print(carrinho)#[('Produto 1', 30), ('Produto 2', 20), ('Produto 3', 50)]

print(total)#[30, 20, 50]
