# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)
class Pessoa:
    def __init__(self, nome):#aqui criase os atributos que depois serao usados(nome,idade,peso)
        self._nome = nome

    @property#definindo um astributo e chama como se chama as funcoes p1.nome
    def nome(self):
        return self._nome#tranforma a variavel para nao se chamar de fora do escopo

    @nome.setter# @variavel criada no getter acima .setter
    def nome(self, nome):
        self._nome = nome#seta as configuracoes e modificacoes

    @property
    def sobrenome(self):
        return 'DESCONHECIDO'


p1 = Pessoa('Otávio')
print(p1.nome)
print(p1.sobrenome)