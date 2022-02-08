from zipfile import ZipFile
import os

# Para caminhos com barra invertida (\), utilize r
caminho = r'/home/dwolter/Documentos/PycharmProjects/pythonProject1'

# ESCREVE
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        #listdir apenas os arquivos escritos no diretorio, nao exibe sub pastas dentro.
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
        print(caminho_completo)