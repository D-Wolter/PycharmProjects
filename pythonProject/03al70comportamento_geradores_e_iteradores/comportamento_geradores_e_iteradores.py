
nome= 'daniel Wolter'
iterador = iter(nome)

try:
    print(next(iterador))#d
    print(next(iterador))#a
    print(next(iterador))#n
    print(next(iterador))#i
except:
    pass

print('cade os valores')
for valor in iterador:#temos a mesma funcao acima com for consumindo o que sobrou da iteracao
    print(valor)
    # e
    # l
    #
    # W
    # o
    # l
    # t
    # e
    # r


