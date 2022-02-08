lista = [
    [1,3,5,7,9],
    [2,4,6,8],
    [11,13,15,17],
    [10,12,14,16]
]

for v in lista:
    print(v[0], v[1])

lista1 = [
    [0, 'Daniel'],
    [1, 'Wolter'],
    [2, 'Martins'],
]
for indice, valor in lista1:# funcao enumarete faz o mesmno desse comando
    print(indice, valor)

lista2 = ['Daniel', 'Wolter', 'Martins']
for indice, valor in enumerate(lista2):
    print(indice, valor)

lista3 = ['Daniel', 'Wolter', 'Martins']

n1, n2 , n3 = lista3
print(n2)
