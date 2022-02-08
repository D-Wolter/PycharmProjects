from zipfile import ZipFile
import os

# Para caminhos com barra invertida (\), utilize r
caminho = r'/home/dwolter/Documentos/PycharmProjects'

# ESCREVE
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
        #print(caminho_completo)
# criando zip mantendo a estruturas de diretorios

with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
