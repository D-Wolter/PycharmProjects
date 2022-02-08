'''
foi criado a classe cliente, o endereço ficou definido como uma classe diferente(aconselhavel)
 porem o endereço ficou subordinado a classe cliente, se mandar apagar o cliente ele apaga tambem o endereço,
 inicialmente criado em outra classe mais atrelado a cliente.
'''
class Cliente:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')