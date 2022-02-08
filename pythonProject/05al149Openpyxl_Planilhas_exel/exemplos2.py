import openpyxl

pedidos = openpyxl.load_workbook('pedidos.xlsx')
nome_planilhas = pedidos.sheetnames
planilha1 = pedidos['Página1']

for linha in planilha1['a1:c4']:
    for coluna in linha:
        print(coluna.value)
        # pedido
        # id_produto
        # preco
        # 1.0
        # 1002.0
        # 50.0
        # 2.0
        # 1005.0
        # 32.25
        # 3.0
        # 1200.0
        # 89.99
        #

