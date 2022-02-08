while True:
    print()
    num1 = input('digite um numero ')
    operador = input('digite um operador ')
    num2 = input('digite outro numero ')


    if not num1.isnumeric() or not num2.isnumeric():
        print('digite apenas numeros')
        continue

 #   if not operador == '+':
  #      print('voce deve escolher + - / *')
  #      continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('voce deve escolher o operador + - / *')
    sair = input('deseja Sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
    if sair == 'n':
        continue

    print('by dwolter')