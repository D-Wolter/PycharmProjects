#definindo funcoes com def

# def saudacao():
#     print('helo')
#
# #chama variavel para a funcao do escopo def
# saudacao()
# saudacao()

def correcao(msg='ola', nome="daniel"):
    nome = nome.replace('a', '4')
    nome = nome.capitalize()
    msg = msg.replace('a', '4')
    msg = msg.capitalize()
    return f'{msg} {nome}'

variavel = correcao()

print(variavel)