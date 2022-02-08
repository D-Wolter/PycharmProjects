# solicitamos dois numero prfa fazer contas, para nao quebra cod usamos try repetidamente
#em todos casos contornaveis, se nao for contornavel vai para except pass

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
    numero = converte_numero(input('Digite um numero'))

    if numero is None:
        print('isso nao eh um numero')
    else:
        print(numero * 2)

