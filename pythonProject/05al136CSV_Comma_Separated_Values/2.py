

import csv

with open ('clientes.csv', 'r') as arquivo:
    dados = csv.DictReader(arquivo)
    #next(dados)#pular primeira linha de clientes.csv

    for dado in dados:
        print(dados(dado['Nome'], dado["E-mail"]))