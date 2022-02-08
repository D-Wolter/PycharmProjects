def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converte_numero(input('digite um numero: '))

    if numero is None:
        print('Erro iiso nao eh um numero')
    else:
        print(numero * 0)