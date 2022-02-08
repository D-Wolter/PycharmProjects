frase = ('O rato roeu a roupa do rei')
letra = ('r')
contador = 0

for valor in frase:
    if valor == letra:
        contador = contador + 1

print(f'A letra {letra} apareceu {contador} vezes na frase')