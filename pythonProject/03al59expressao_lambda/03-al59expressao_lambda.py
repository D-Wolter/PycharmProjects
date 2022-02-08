# def func_multiplica(valor1, valor2):
#     return valor1 * valor2
#
# total = func_multiplica(2,2)
# print(total)


#codigo lambda igual a funcao acima
#multiplicar = lambda x, y: x * y
#print(multiplicar(2,2))
#4
#lambda ultilizado quando vc preciasa passar um parametro de uma funcao a outra


lista_produtos = [
    ['tv', 900],
    ['carro', 15000],
    ['moto', 9600],
    ["bike", 500],
]
#definindo funcao para exibir em ordem pelo valor
#def listar(produto):
#    return produto[1]

#lista_produtos.sort(key=listar)
#lista_produtos.sort(key=listar reverse=True)aqui exibe pelo valor mas decrescente
#print(lista_produtos)
#[['bike', 500], ['tv', 900], ['moto', 9600], ['carro', 15000]]


#aqui temos o mesmo resultado chamando lambda
lista_produtos.sort(key=lambda iten: iten[1])
print(lista_produtos)

#outra forma seria assim pra nao editar a lista original
print(sorted(lista_produtos, key=lambda i: i[1]))