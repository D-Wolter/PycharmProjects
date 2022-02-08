#!/usr/bin/env python

"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
Palavra = 'perfume'
reveladas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    tentativa = input('Digite uma letra: ')

    if len(tentativa) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    reveladas.append(tentativa)

    if tentativa in Palavra:
        print(f'UHUULLL, a letra "{tentativa}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{tentativa}" NÃO EXISTE na palavra secreta.')
        reveladas.pop()

    secreto_temporario = ''
    for letra in Palavra:# for é um laço que faz iteracao das string
        if letra in reveladas:
            secreto_temporario += letra
        else:
            secreto_temporario += '*'# +=concatena na string na ultima casa

    if secreto_temporario == Palavra:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if tentativa not in Palavra:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
