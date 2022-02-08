#https://docs.python.org/3/library/json.html

from dados import *
import json

lista = [1,2,3,4,5,6,7]
dados_json = json.dumps(lista)#json.dumps(nomedoaqrquivo_a_converter)metodo para passar de python p json
print(dados_json)
#json
#[1, 2, 3, 4, 5, 6, 7]
print(type(dados_json))
#<class 'str'>

