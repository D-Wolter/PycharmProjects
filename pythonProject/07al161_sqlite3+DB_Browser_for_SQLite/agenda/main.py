import sqlite3


class AgendaDB:

    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        # variavel chamar conexao com arquivo
        self.cursor = self.conn.cursor()
        #definir cursor para metodos abaixo


    def inserir(self, nome, telefone):

        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
         # insere na agenda os valore
        self.cursor.execute(consulta, (nome, telefone))
        #                         indica nome e telefone aqui
        self.conn.commit()#salvar


    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
         #                            por ser tupla deixa uma virgula apos
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.buscar('luiz')
