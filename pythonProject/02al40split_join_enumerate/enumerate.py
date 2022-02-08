#enumerate

string = 'O Brasil é Penta'
lista = string.split(' ')

for v1, v2 in enumerate(lista):
    print(v1, v2)# print(v1, v2,(lista[v1]))

    #0 O
    #1 Brasil
    #2 é
    #3 Penta