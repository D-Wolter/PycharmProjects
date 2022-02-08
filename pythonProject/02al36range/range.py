"""
laço while usasse em ocasioes em que nao se babe o fim laço for para acoes infinitas
For in
iterando strings com for funcao range(start=0, stop, step
"""
#laço for
#laço while
#texto = 'Python'
#c = 0
#while c < len(texto):
#    print(texto[c])
#    c += 1


#laço for com mesma funçao
#texto = 'Python'

#for letra in texto:
#    print(letra)


#laço for com mesma funçao enumerando
#texto = 'Python'

#for n, letra in enumerate(texto):
#    print(n, letra)


#range funcao range(start=0, stop, step
#lacço for, chama n numeros, em classificaçao# (numero de inicio, numero de chegada, de quantas casas pula
#for numero in range (20, 10, -1):
#    print(numero)

texto ='Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string = letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)