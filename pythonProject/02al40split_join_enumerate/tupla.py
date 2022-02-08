# tupla só tem indice 0 alocado, tupla e tipo a lista mais infoma na primeira caixa de indice seu valo
#e faz o indice 0 e o indice 1 com informacao agrupada sem mais indices, tuplas nao se pode alterar o valores

lista = [
    #   0       1         2indice da lista filhas
    ['dani', 'andre', 'airton'],#0 da lista mae
    ['lucia', 'jordam', 'heron'],#1 da lista mae
    ['neusa', 'ary', 'cris'],#2 da lista mae
]

enumerada = list(enumerate(lista))#cria uma tupla
#print(enumerada)
#  0     1        2         3        1      1        3
#[(0, ['dani', 'andre', 'airton']), (1, ['lucia', 'jordam', 'heron']), (2, ['neusa', 'ary', 'cris'])]
#print(enumerada[0][1])
#['dani', 'andre', 'airton']
print(enumerada[0][1][0])# na [1] do meio so pode ter o valor 1 ([(0, ['dani', 'andre', 'airton'])
#na tupla tem indice 0 e 1 alocados
#para acessar deve se por a terceira [] e escolher o indice a partir do 0