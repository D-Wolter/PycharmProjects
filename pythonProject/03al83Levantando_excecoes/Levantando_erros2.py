
def divide(n1, n2):#dessa forma levantamos o erro sem parar o cod
    if n2 == 0:#se n2 for igual a zero
        raise ValueError("n2 nao pode ser 0 ")
    return n1 / n2



try:
    print(divide(n1=2,n2=1))
except ValueError as error:
    print('Voce esta tentando dividir por zero')
    print('log:', error)