def func(*args):
    print(args)

#lista = [1,2,3,4,5]
#func(*lista, 10, 20,30)#adicionar itens dentro da tupla

lista = [1,2,3,4,5]
lista2 = [10, 20,30]
func(*lista, *lista2)#mescla as duas listas na tupla