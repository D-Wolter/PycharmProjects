


Palavra_secreta = 'perfume'
acertos = []

while True:
    letra = input('indique uma letra')

    if len(letra) > 1:#se for maior que um
        print('digite apenas uma letra')
        continue

    acertos.append(letra)#adiciona o input a letras

    if letra in Palavra_secreta:
        print(f'{letra} a letra existe na palavra')
    else:
        print(f'a letra {letra} nao existe na palavra')


    print(acertos)



