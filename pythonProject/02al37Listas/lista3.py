valores = [334, 567, 435, 678]

print( max(valores) )#exibe valor mais alto
print( min(valores) )#exibe valor mais baixo


pares = list(range(0,100, 2))#listando pares
impar = list(range(1,101, 2))#listyando impares
print(pares)
print(impar)

for valor in pares:#iterando valores range
    print(valor)