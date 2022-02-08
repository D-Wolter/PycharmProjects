import re


def remover_caract(numero):
    return re.sub(r'[^0-9]', '', numero)
