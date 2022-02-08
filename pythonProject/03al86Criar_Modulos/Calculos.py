
import math

PI = math.pi

def dobralista(lista):
    return [x*2 for x in lista]

def mutiplica(lista):
    r =1
    for i in lista:
        r *= i
    return r

if __name__=='__main__':#se faz esse laco porque __main__ so retorna de __name__ aqui dentro do arquivo
    #quando esse aquivo for importado esse escopo nao aarece
    lista = [1,2,3,4,5]
    print(dobralista(lista))
    print(mutiplica(lista))
    print(PI)


print(__name__)#Aqui dentro do arquivo esse __name retorna __main__, quando se importa esse arquivo comno
#modulo, dai esse name retorna o nome desse arquivo (Calculos)
#__main__