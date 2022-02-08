#converte dicionario python prara dicionadio json e vice versa

from dados import *
import json

with open('clientes.json', 'W') as arquivo:#convertendo dic python pra dic json
    json.dump(clientes_dicionario, arquivo)