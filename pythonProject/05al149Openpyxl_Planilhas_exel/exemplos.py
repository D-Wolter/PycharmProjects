import openpyxl

pedidos = openpyxl.load_workbook('pedidos.xlsx')
nome_planilhas = pedidos.sheetnames
planilha1 = pedidos['Página1']

print(planilha1['b4'])
#<Cell 'Página1'.B4>

print(planilha1['b4'].value)
#1200.0

print(planilha1['b'])
#(<Cell 'Página1'.B1>, <Cell 'Página1'.B2>, <Cell 'Página1'.B3>, <Cell 'Página1'.B4>, <Cell 'Página1'.B5>, <Cell
# 'Página1'.B6>, <Cell 'Página1'.B7>, <Cell 'Página1'.B8>, <Cell 'Página1'.B9>, <Cell 'Página1'.B10>, <Cell 'Página1'
# .B11>, <Cell 'Página1'.B12>, <Cell 'Página1'.B13>, <Cell 'Página1'.B14>)

for campo in planilha1['b']:
    print(campo.value)
    # id_produto
    # 1002.0
    # 1005.0
    # 1200.0
    # None
    # None
    # None
    # None
    # None
    # None
    # None
    # None
    # None
    # None
    #


