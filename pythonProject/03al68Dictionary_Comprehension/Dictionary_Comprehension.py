
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
]
#      .uper maisc *2 vezes dois
d1 = {x.upper(): y*2 for x, y in lista}#fazendo a comprensao de dicionario chama x e y agrega a
#modificacao for x y in lista
print(d1)
#{'CHAVE1': 'valor1valor1', 'CHAVE2': 'valor2valor2'}