"""
TIPOS DE DADOS primitivos
STR - STRING - TEXTOS 'ASSIM' "ASSIM"
int - inteiros - valore 123456 0 -12
float - real/ponto flutuante valores com ponto 1.1  0.3
bool - booleano/logico - True/False 10 == 10 (valor 0 ou sem valor =false

"""

print(type(10))# type exibe o tipo de dados <class 'int'>
#<class 'int'>

print(type(1.0))
#<class 'float'>

print(type('daniel'))
#<class 'str'>

print(type(10 == 10))
#<class 'bool'>

print('daniel', type('daniel'))
#daniel <class 'str'>

print(10, type(10))
#10 <class 'int'>

print(22.2, type(22.2))
#22.2 <class 'float'>

print(10 == 10, type(10 == 10))
#True <class 'bool'>

#converter os formato  primitivos
print('daniel', type('daniel'), bool('daniel'))
#daniel <class 'str'> True

print('10', type('10'), type(int('10')))  #int() converteu string numerica em inteiro
#10 <class 'str'> <class

print('10.1', float('10.1'))

print('danielWolter')