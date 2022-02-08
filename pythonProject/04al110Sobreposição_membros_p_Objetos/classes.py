class Pessoa:#superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):#superclasse
        print(f'{self.nomeclasse} superclasse')


class Cliente(Pessoa):#subclasse
    def spc(self):#subclasse
        print(f'{self.nomeclasse} esta com nome no spc')

    def falar(self):
        print('subclasse pessoa')

# class ClienteVIP(Cliente):#subclasse de cliente
#     def falar(self):#sobrescrever a funcao falar de cliente aciima
#         Pessoa.falar(self)#chama funcao falar de pessoa
#         Cliente.falar(self)#chama funcao falar de cliente
#         print('subclasse cliente')#executa funcao falar clientevip

class ClienteVIP(Cliente):
    def __init__(self, nome, idade, credito):
        Pessoa.__init__(self, nome, idade)
        self.credito = credito

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} voce tem um credito de {self.credito} Reais disponivel')





