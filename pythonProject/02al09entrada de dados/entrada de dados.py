'''
entrada de dados
'''

nome = input("qual o seu nome? ")#por padrao entra como classe string nao aceite numeros
idade = input("qual sua idade ")
nasc = 2021-int(idade)#para por numero podese fazer um cast e converter em inteiro

print(f'{nome} tem {idade} anos.'
      f'{nome} nasceu em {nasc}.')

num_1 = int(input('digite um nujmero: '))# pode fazer um cast assim
num_2 = input('digite outro numero: ')
num_2 = int(num_2)                       #e pode fazer outro assim

print(f'o resultado da soma é  {num_1 + num_2} ')