"""o encapsulamento serve para proteger algumas partes de seu codigo, classe, ou metodo.
como python nao eh voltado a objetos como java c++ php
em programacao em geral tem partes do codigo nomeadas (public , protected, private)

public pode ser acessado dentro e fora da classe
protected sao atributos que so podem ser acessado dentro da classe, ou filhas da classe
private so esta disponivel dentro da classe
_ em python usa para deixar meio oculto protected
__em python usa para deixar privado
"""

class BaseDeDados:
    def __init__(self):#init eh o mais proximo de um construtor e vamos adicionar ao dicionario o banco de dados
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'] [id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'daniel')
bd.inserir_cliente(2, 'luana')
bd.inserir_cliente(3, 'tiago')
bd.apaga_cliente(3)
bd.__dados = 'outra coisa'#aqui criamos uma chave e valor que esta no escopo global e nao tem nada
# em haver cos os __dados da classe costrutora
print(bd.__dados)
#outra coisa

print(bd._BaseDeDados__dados)
#{'clientes': {1: 'daniel', 2: 'luana'}}

#bd.lista_clientes()
