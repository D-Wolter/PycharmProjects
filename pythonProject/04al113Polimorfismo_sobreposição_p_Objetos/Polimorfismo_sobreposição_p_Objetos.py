'''
Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse
tenham metodos iguais (de mesma assinatura) mas comportamentos diferentes
mesma assinatura = mesma quantidade e tipo de parametros
'''

#criando execoes para erros
class TaErradoError(Exception):
    pass

def testar():
    raise TaErradoError('errado')

try:
    testar()
except TaErradoError as error:
    print(f'Erro {error}')
