'''
contar caracteres dentro de string
nao funciona com float e int

usuario = input('digiteu seu nome de usuario')
qtd_carcters = len(usuario)

if qtd_carcters < 6:
    print('seu usuario deve ter no minimo 6 ctrters')
else:
    print('cadastro efetuado com sucesso')
'''
#fazer a soma de duas variantes
primeironome = input('digite seu nome ')
segundonome = input('digite su sobrenome ')
senha = input('digite uma sernha')

print(f' a quant de cardtado foi {len(primeironome) +len(segundonome)}')
#len nao funciona com numeros inteiros ou ponto flutuant float. e bool tamb nao true or false
#por baixo o python usa o len abreviado para funcao __len__
#os dois cod abaixo sao iguais
print(len(primeironome))
print(primeironome.__len__())

#lembra que input so entra como string e devemos converter em outros formatos
#nome = input("igite um nome usuario")
#senha = input('digite uma senha')
#nome = int(nome)
#str.isdecimal()
#str.isdigit()
#str.isnumeric()

#saber se uma str pode ser convertida em numero retorna true or false
#verificando se a senha pode ser convertida em numero
#so funciona com numeros positivos
print(senha.isnumeric())
print(senha.isdigit())
print(senha.isdecimal())

if senha.isdigit():
    senha = int(senha)

    print(senha + senha)
else:
    print("sua senha deve ser numerica")

"""
codigo que vamos aprende depois para ultilizar numeros ponto flutuantes na contas

import re


#verificando se uma string pode ser convertida para ponto flutuante 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
    

#verificando se uma string pode ser convertida em numero inteiro
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False


#verificando se uma string pode ser convertida em int or float 
def is_number(val):
    return is_int(val) or is_float(val)
 """