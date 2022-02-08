import os

caminho = '/home/dwolter/Documentos/PycharmProjects/pythonProject1'
for arquivo in os.walk(caminho):
    # walk arquivos escritos no diretorioe  sub pastas adentro.
    print(arquivo)