'''
split - dividir string
join - juntar uma lista
enumerate - enumerar elementos da lista e objetos iteraveis
'''


#split
string = 'daniel wolter martins'
lista1 = string.split(' ')# funcao split dividi a string por exemplo pelo espaço cria uma lista

print (lista1)#lista criada pelo split
#['daniel', 'wolter', 'martins']

for valor in lista1:#iterando lista criada
    print(valor)
#daniel
#wolter
#martins

# contar quantas vezes um carcter se repete dentro de uma string
for valor in string:#iterando string
    #print(lista1.count(valor))
    print(f' a pavavra {valor} apareceu {string.count(valor)} x na frase.')#mesmo cod acima f string
# a pavavra d apareceu 1 x na frase.
#  a pavavra a apareceu 2 x na frase.
#  a pavavra n apareceu 2 x na frase.
#  a pavavra i apareceu 2 x na frase.
#  a pavavra e apareceu 2 x na frase.
#  a pavavra l apareceu 2 x na frase.
#  a pavavra   apareceu 2 x na frase.
#  a pavavra w apareceu 1 x na frase.

