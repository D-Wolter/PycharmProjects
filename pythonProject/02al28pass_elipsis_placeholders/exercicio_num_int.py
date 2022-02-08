numero_int = input('Digite um numero inteiro')

if numero_int.isdigit():
    numero_int = int(numero_int)

    if numero_int % 2 == 0:
        print('o numero e par')
    elif numero_int % 1 == 0:
        print('o numero e impar')
else:
    