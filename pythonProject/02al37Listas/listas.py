'''
Listas em Python
fatiamento
append, insert, pop, del clear, extend, +
min, max
range
'''
#indice     0         1          2         3       4     5     6
#indice-    7         6          5         4       3     2     1
lista = ['Daniel', 'Wolter', 'Martins',            40, 1.87, True]
string = 'Daniel Wolter Martins'
primeiro_nome = lista[0]
segundo_nome = lista[1]
terceiro_nome = lista[2]
idade = lista[3]
altura = lista[4]
vivo_ainda = lista[5]

print(lista[0:3])
print(lista[3:])

print(lista[0], lista[1],lista[2])
print('pirmeiro nome', primeiro_nome, ',segundo nome',segundo_nome, ',terceiro nome', terceiro_nome, ',idade de', idade, 'anos,', altura, 'de altura, aindaesta vivo', vivo_ainda)