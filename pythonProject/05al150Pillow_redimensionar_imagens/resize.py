'''

'''


import os#NESSESSSARIO P ACESSAR DIRETORIO E PERCORER PASTAS
from PIL import Image#MANIPULAR IMAGENS


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder): #SE NAO FOR UM FOLDER
        raise NotADirectoryError(f'{main_images_folder} não existe.')

    for root, dirs, files in os.walk(main_images_folder):#OS.WALK NO DIRETORIO INDICADO
        for file in files:#ARUIVO EM ARQUIVOS
            file_full_path = os.path.join(root, file)#CAMINHO COMPLETO JUNTA FILE COM CAMINHO NA PASTA
            file_name, extension = os.path.splitext(file)#NOME DO ARQUIVO E NOME DA EXTENSAO LADO A LADO

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)#ESCREVER NA RAIZ COM A STRING _CONVERTED

            # if converted_tag in file_full_path:
            #     os.remove(file_full_path)
            #
            # continue

            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} já existe.')
                continue

            if converted_tag in file_full_path:
                print('Imagem já convertida.')
                continue

            img_pillow = Image.open(file_full_path)#ABRINDO EDITOR

            width, height = img_pillow.size
            new_height = round((new_width * height) / width)

            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS
            )

            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70,#REDUCAO DE QUALIDADE
                exif=img_pillow.info['exif']
            )

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()#FECHANDO EDITOR

            # os.remove(file_full_path)


if __name__ == '__main__':#FUNCAO PRINCIPAL RECEBE CAMINHO DA PASTA main_images_folder = ('')
    main_images_folder = '/home/dwolter/PycharmProjects/pythonProject/05al150Pillow_redimensionar_imagens/100CANON'
    main(main_images_folder, new_width=1920)