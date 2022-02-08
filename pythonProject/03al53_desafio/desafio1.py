'''
Crie uma funcao que exibe uma saudacao com parametros saudacao e nome
'''

while True:
    nome = input("Qual seu nome  ")
    saudacao = 'Muito Boa Tarde'

    if nome:
        nome = nome.capitalize()
        print(saudacao, nome)
    else:
        print('Vc deve digitar um numero')

    sair = input('deseja Sair? [s]im ou [n]ão: ')


    if sair == 's':
        break
    if sair == 'n':
        continue