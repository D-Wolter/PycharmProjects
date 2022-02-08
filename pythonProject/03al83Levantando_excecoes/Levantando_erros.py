
def divide(n1, n2):#dessa forma levantamos o erro sem parar o cod
    if n2 == 0:#se n2 for igual a zero
        raise ValueError("n2 nao pode ser 0 ")
    return n1 / n2

print((divide(2,0)))
#     raise ValueError("n2 nao pode ser 0 ")
# ValueError: n2 nao pode ser 0
