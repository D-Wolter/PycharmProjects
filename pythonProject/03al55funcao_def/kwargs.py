def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])#kwargs cria valores alteraveis acoplado na tupla

#lista = [1,2,3,4,5]
#func(*lista, 10, 20,30)#adicionar itens dentro da tupla

lista = [1,2,3,4,5]
lista2 = [10, 20,30]
func(*lista, *lista2, nome='luiz', sobrenome="miranda")#aqui chama os valores
#(1, 2, 3, 4, 5, 10, 20, 30)
#luiz miranda