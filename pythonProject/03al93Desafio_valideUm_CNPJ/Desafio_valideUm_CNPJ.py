# template para remover carcteres que nao sao numeros(modulo importavel
# cnpj = "04.252.011/0001"
import re


def remover_caract(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
    # re regular expressions sub substituir, ^0-9 diferente de 0 a 9, vai substituir por nada

# codigo acima resume esse abaixo

# def remover_caract(cnpj):
# cnpj = cnpj.replace('/', '')
# cnpj = cnpj.replace('.', '')
# cnpj = cnpj.replace('-', '')
# return cnpj
