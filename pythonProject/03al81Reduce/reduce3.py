from dados import produtos, pessoas, lista
from functools import reduce

#saber a media de idade das pessoas
soma_idades = reduce(lambda acumulador, idade: idade['idade'] + acumulador, pessoas, 0)
print(soma_idades / len (pessoas))
#39.9
#media de idade