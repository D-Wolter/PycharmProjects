#iteraveis arquivos que podem ser iterados
#lista = 345 #numero int nao sao iteraveis

lista = [0,3,5,67]

print(hasattr(lista, '__iter__'))#comando verifica se é iteravel retorna True Boleano

#se é iteravel é possivel dar for