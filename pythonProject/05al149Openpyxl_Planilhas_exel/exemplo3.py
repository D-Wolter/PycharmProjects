import openpyxl

pedidos = openpyxl.load_workbook('pedidos.xlsx')
nome_planilhas = pedidos.sheetnames
planilha1 = pedidos['Página1']

for linha in planilha1:
    print(linha[0].value, linha[1].value, linha[2].value, linha[3].value,)

for linha in planilha1:
    if linha[0].value is not None:
        print(linha[0].value, end=' ')
    if linha[1].value is not None:
        print(linha[1].value, end=' ')
    if linha[2].value is not None:
        print(linha[2].value, end=' ')
    if linha[3].value is not None:
        print(linha[3].value)
     #pedido id_produto preco 1.0 1002.0 50.0 2.0 1005.0 32.25 3.0 1200.0 89.99
