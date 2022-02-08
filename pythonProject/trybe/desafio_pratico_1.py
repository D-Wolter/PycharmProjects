#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'calculadoraAdicaoSubtracao' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER numero
#  2. INTEGER outroNumero
#  3. STRING operacao
#

zero = 0


def calculadoraAdicaoSubtracao(numero, outroNumero, operacao):
    if operacao == '+':
        return (numero + outroNumero)
    elif operacao == '-':
        return (numero - outroNumero)
    elif operacao != '+' or '-':
        return (zero)


if __name__ == '__main__':