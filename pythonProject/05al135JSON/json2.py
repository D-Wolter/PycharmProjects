#https://docs.python.org/3/library/json.html

from dados import *
import json


# dados_json = json.dumps(clientes_dicionario)
# print(dados_json)
# #{"1": {"nome": "Luiz Ot\u00e1vio", "sobrenome": "Miranda", "idade": 25, "altura": 1.8, "peso": 80.53}, "2": {"nome": "Maria", "sobrenome": "Oliveira", "idade": 52, "altura": 1.67, "peso": 57}, "3": {"nome": "Pedro", "sobrenome": "Faria", "idade": 32, "altura": 1.95, "peso": 113}}

dados_json = json.dumps(clientes_dicionario, indent=10)#indent+10 distancia a esquerda no print
print(dados_json)
# {
#     "1": {
#         "nome": "Luiz Ot\u00e1vio",
#         "sobrenome": "Miranda",
#         "idade": 25,
#         "altura": 1.8,
#         "peso": 80.53
#     },
#     "2": {
#         "nome": "Maria",
#         "sobrenome": "Oliveira",
#         "idade": 52,
#         "altura": 1.67,
#         "peso": 57
#     },
#     "3": {
#         "nome": "Pedro",
#         "sobrenome": "Faria",
#         "idade": 32,
#         "altura": 1.95,
#         "peso": 113
#     }
# }
