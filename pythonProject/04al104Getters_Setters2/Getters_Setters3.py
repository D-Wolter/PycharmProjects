# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)
#criase o init __nome pra varaivel nao ser crudas com a entrada e saida
class Pessoa:
    def __init__(self, nome):#aqui criase os atributos que depois serao usados(nome,idade,peso)
        self._nome = nome#aqui eh apenas referencia para poder usar getter e setter

    @property#definindo um astributo e chama como se chama as funcoes p1.nome
    def nome(self):
        return self._nome#tranforma a variavel para nao se chamar de fora do escopo

    @nome.setter# @variavel criada no getter acima .setter
    def nome(self, nome):
        self._nome = nome#seta as configuracoes e modificacoes

    @property
    def sobrenome(self):
        return 'segundoNome'


p1 = Pessoa('Otávio')
print(p1.nome)
print(p1.sobrenome)