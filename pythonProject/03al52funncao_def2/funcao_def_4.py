def f(var):
    print(var)#definir uma funcao

def dumb():
    return f#chama o laço de funcao acima

var = dumb()#define variavel a chamar o dumb que chama a funcao
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('Blaaaa')