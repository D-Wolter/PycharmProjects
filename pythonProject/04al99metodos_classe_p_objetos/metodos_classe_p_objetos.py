class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

#p1 = Pessoa('luis', 32)
p1 = Pessoa.por_ano_nascimento('luis', 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

# <__main__.Pessoa object at 0x00000251BA380FA0>
# luis 32
# 1987
