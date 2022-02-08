
def func(*args):
    print(args)#empacotador e desepacotador

lista = [1,2,3,4,5]
#n1, n2, *n = lista#n1 n2 desempacotou e *n  empacotiou o questo do itens em uma lista
#print(n1, n2, n)
#1 2 [3, 4, 5]

print(*lista, sep='@')# * desempacotou a lista, sep='@' usar @ como separador
#1@2@3@4@5