lista = [
    #   0       1         2indice da lista filhas
    ['dani', 'andre', 'airton'],#0 da lista mae
    ['lucia', 'jordam', 'heron'],#1 da lista mae
    ['neusa', 'ary', 'cris'],#2 da lista mae
]

#print(lista[2])
#['neusa', 'ary', 'cris']
print(lista[1][2])# print primeiro[] indice 1 da lista mae e segunda [] indice 2 da lista filha
#heron

enumerada = enumerate(lista)# lista mae cri obj enumerate para vc poder iterar sobre eles(usar o laço for)
print(enumerate)
#<class 'enumerate'>
#<enumerate object at 0x000001FF25C67A00>
print(list(enumerada))#funcao list criou a lista da varianre enumerada
#[(0, ['dani', 'andre', 'airton']), (1, ['lucia', 'jordam', 'heron']), (2, ['neusa', 'ary', 'cris'])]