import os

caminho = '/home/dwolter/Documentos/PycharmProjects/pythonProject1'
for arquivo in os.listdir(caminho):
    # listdir apenas os arquivos escritos no diretorio, nao exibe sub pastas dentro.
    print(arquivo)