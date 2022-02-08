lista = [
    #   0       1         2indice da lista filhas
    ['dani', 'andre', 'airton'],#0 da lista mae
    ['lucia', 'jordam', 'heron'],#1 da lista mae
    ['neusa', 'ary', 'cris'],#2 da lista mae
]

for v1 in enumerate(lista, 53):#enumera a partir de 53, nao altera indice
    valor_enu, minha_li = v1
    #print(valor_enu, minha_li)
    #53['dani', 'andre', 'airton']
    #54['lucia', 'jordam', 'heron']
    #55['neusa', 'ary', 'cris']
    #print(minha_li)
    #['dani', 'andre', 'airton']
    #['lucia', 'jordam', 'heron']
    #['neusa', 'ary', 'cris']
    nome1, nome2, nome3 = minha_li
    print(nome2, nome3)
    #andre airton
    #jordam heron
    #ary cris