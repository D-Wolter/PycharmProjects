class BaseDeDados:
    def __init__(self):#init eh o mais proximo de um construtor e vamos adicionar ao dicionario o banco de dados
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:#se a informacao nao tiver na base de dados
            self.dados['clientes'] = {id: nome}#cria um cliente
        else:
            self.dados['clientes'].update({id: nome})#se a chave ja existir na base de dados atualiza a base

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'] [id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'daniel')
bd.inserir_cliente(2, 'luana')
bd.inserir_cliente(3, 'tiago')
bd.apaga_cliente(3)
bd.lista_clientes()


#print(bd.dados)
#{'clientes': {1: 'daniel', 2: 'luana', 3: 'tiago'}}


