frase = 'o rato roel a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
qual_letra_sera_maiuscula = input('qual letra deseja ser maiuscula')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == qual_letra_sera_maiuscula:#letra atual
        nova_string += qual_letra_sera_maiuscula.upper()#letra substiytuida .upper converte maisc
    else:
        nova_string += letra
    contador += 1

print(nova_string)
