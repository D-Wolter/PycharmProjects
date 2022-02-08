import sqlite3

class AgendaDB:
    def __init__(self, arquivo):#i
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
