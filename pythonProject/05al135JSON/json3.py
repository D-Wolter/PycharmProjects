#converter json para python

from dados import *
import json

dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave)
    print(valor)

# 1
# {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 25, 'altura': 1.8, 'peso': 80.53}
# 2
# {'nome': 'Maria', 'sobrenome': 'Oliveira', 'idade': 52, 'altura': 1.67, 'peso': 57}
# 3
# {'nome': 'Pedro', 'sobrenome': 'Faria', 'idade': 32, 'altura': 1.95, 'peso': 113}
