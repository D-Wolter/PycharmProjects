nome = 'daniel wolter'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))#d
print(next(gerador))#a
print(next(gerador))#n
print(next(gerador))#i
print( )
for letra in gerador:
    print(letra)
    # e
    # l
    #
    # w
    # o
    # l
    # t
    # e
    # r
print(next(gerador))
#StopIteration