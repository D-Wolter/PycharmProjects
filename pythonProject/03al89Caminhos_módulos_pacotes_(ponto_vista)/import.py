#template para importar pasta um nivel acima muito usado quando fazemos testes

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../' # a cada ../ sobe um nivel se quiser subir tre niveis por exemplo ../../../
            )
        )
    )
except ImportError:
    raise



from Filter.dados import lista
print(lista)