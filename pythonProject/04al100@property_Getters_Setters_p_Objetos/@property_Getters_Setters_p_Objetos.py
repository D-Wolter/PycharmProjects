
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco *(percentual / 100))




    # Getter obtem o valor que entrou como string
    @property
    def preco(self):
        return self._preco #aqui nao pode ter o mesmo nome de variavel
    # Setter seta o valor no formato de ponto flutuante
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


    @property#ombet nome em caixa alta
    def nome(self):
        return self._nome

    @nome.setter# seta um novo nome com primeira maiuscula
    def nome(self, valor):
        self._nome = valor.title()



p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)
#45.0

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco)
#13.5