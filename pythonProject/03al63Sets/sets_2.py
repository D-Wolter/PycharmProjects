'''
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda
symmetric_difference ^ (elementos que estao nos dois sets, mas nao em ambos)
set ajuda a eleminar elementos duplicados na lista
sets usando {} ,sets eh como dicionario ,lista usando as {} e so tem valor sem chaves
alem de nao ter chaves nao da para puxar por indice e nescessario iterar para desempacotar
'''

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2# Funcao | une
#s3 = s1 union s2     #pode escreverassim tambem
print(s3)
#{1, 2, 3, 4, 5, 6, 7}

s4 = s1 & s2# & exibe elementos que estao presentes nos dois sets
print(s4)
#{1, 2, 3, 4, 5}

s5 = s1 - s2#mostra algum elemento que so esta presente no set da esquerda
print(s5)
#{7}
s6 = s2 - s1# pode se inverter as variantes
print(s6)
#{6}

s6 = s1 ^ s2# elementos que estao presentes em apenas um dos sets
print(s6)
#{6, 7}
