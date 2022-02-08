
import csv

with open ('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

for dado in dados:
    print(dado)