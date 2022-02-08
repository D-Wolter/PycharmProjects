#desepacotamento

lista = ['Daniel', 'Wolter', 'Martins', 'restaurador', 1,2,3,4,5,6,7,8,100]

n1, n2, n3, *resto_lista, ultima = lista#posso citar variaveis n1 n2 n3. *variavel resto da variavel
# e posso por apos uma variavel ultimo indice da lista
print(n2, resto_lista)
#Wolter ['restaurador', 1, 2, 3, 4, 5, 6, 7, 8, 100]
print(ultima)
#100