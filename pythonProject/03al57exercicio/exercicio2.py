'''
crie uma funcao1 que receba uma funcao2 como parametro e reotrne o valorda
funcao2 executada, faça a funcao1 executar duas funcoes que recebam um numero
diferente de argumentos
'''

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}'

def saudacao(nome, saudacao):
    return f' {saudacao}{nome}'

executando = mestre(fala_oi, 'Daniel')
executando2 = mestre(saudacao, "Luiz", saudacao='bom dia!')
print(executando)
print(executando2)