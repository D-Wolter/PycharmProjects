"""
manipulando strings
* string indices
*fatiamento de string [inici:fim:passo]
*funcoes buit-in len, abs, type, print, etc
essa funcoes podem ser usadas diretamente em cada tipo.
"""

# positivos [0123456789]
nome =      'Daniel wol'
print( nome[7])#para acessar o indice usase [] e o numero da casa decimal
print(nome[:-1])# chama o indice e exclui o ultimo caracter

apelido = nome[0:4]# tirou da casa 0 ate ate a 3 casa lembraqndo que a ultima casa nao aparede
apelido = nome[:4]# pode deixar o valor de partida vazio se partir do inicio
print(apelido)