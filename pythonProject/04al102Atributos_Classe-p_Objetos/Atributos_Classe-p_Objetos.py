
class A:
    variavel_classe = 123

#para mudar o valor da classe
#A.vc = 'Alterado'

a001 = A()
a002 = A()

a001.variavel_classe = 321
# criamos um atributo para essa instancia entao nao usa mais o valor padrao da classe

print(a001.__dict__)
print(a002.__dict__)
print(A.__dict__)

print()

print(a001.variavel_classe)
print(a002.variavel_classe)
print(A.variavel_classe)

