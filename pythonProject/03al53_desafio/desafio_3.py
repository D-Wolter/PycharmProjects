"""
crie uma funcao que receba 2 numeros, o primeiro é um valor e o segundo um percentual
(exemplo 10%). retorne (return) o valor do primerio numero somado do aumento do percentual
"""

# def Valor_total(n1, n2):
#
#     percentual = n1  / 10
#
#     return n1 + percentual
#
# resultado = Valor_total(100,0)
#
# if resultado:
#     print(f'{resultado:.2f}')
# else:
#     print('conta invalida')
#
def aumento_percentual (valor, percentual):
     return (valor + (valor * percentual / 100))

ap = aumento_percentual(50, 10)
print(ap)
ap = aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(200, 10)
print(ap)
ap = aumento_percentual(15, 100)
print(ap)
