#indices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

print(frase[0])
print(frase[2:6])
print(frase[7:11])

while contador < tamanho_frase:

    if contador == 'r':

       nova_string += frase[contador]
       contador += 1

print(nova_string)