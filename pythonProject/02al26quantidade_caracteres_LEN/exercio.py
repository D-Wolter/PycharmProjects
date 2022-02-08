'''
verificando se os numeros sao par ou impar
'''
numero_inteiro = input('digite numero')#solicitando numero

if numero_inteiro.isdigit():#se string pode ser numero
    numero_inteiro = int(numero_inteiro)#convert string em int

    if numero_inteiro % 2 == 0:#verifica se o resto da soma e 2 zeram
        print(f"{numero_inteiro} e par")
    else:#se nao zerar
        print(f"{numero_inteiro} e impar")
else:
    print('isso nao numero')

