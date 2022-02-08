string = " brasil e o pais do roubo, brasil "

# codigo abaixo string dividida por espaço
lista1 = string.split(' ')

palavra = ''
contagem = 0

#depois de dividida cada valor é iterado comando count conta quantas vezes repete
for valor in lista1:
    qtd_vezes = lista1.count(valor)

#depois dedividida laço abaixo
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f' A palavra que apareceu mais é {palavra} ({contagem}x)')
# A palavra que apareceu mais é o (4x)