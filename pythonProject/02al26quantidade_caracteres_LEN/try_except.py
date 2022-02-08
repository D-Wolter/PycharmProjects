num1 = input('digite numero')
num2 = input('digite outro n')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('numero formato invalido')

#soma entre numeros ponto float