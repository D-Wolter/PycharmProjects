texto = 'açucaré'
nova_string = ''

for letra in texto:
    if letra == 'ç':#trocando letras fora do padrao html
        nova_string = nova_string + "c"
    elif letra == 'é':
        nova_string += 'e'

    else:#caso as letras nao estejam listadas no laço acima roda esse
        nova_string += letra

print(nova_string)