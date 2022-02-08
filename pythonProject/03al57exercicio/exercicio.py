'''
crie uma funcao1 que recebe uma funcao2 como parametro e retorne o
valor da funcao2 executada
'''

def ola_mundo():
    return 'ola munda'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)

print(executando)


