"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

soma1 = (lista_a[0]+ lista_b[0])
soma2 = (lista_a[1]+ lista_b[1])
soma3 = (lista_a[2]+ lista_b[2])
soma4 = (lista_a[3]+ lista_b[3])

resultado = (soma1,soma2,soma3,soma4)
print(f' Lista Soma = {resultado}')
