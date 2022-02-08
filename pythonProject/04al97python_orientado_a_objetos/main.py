from python_orientado_a_objetos import Pessoa

p1 = Pessoa("daniel", 40)
p2 = Pessoa('Luana', 30)
p1.comer('maça')
p1.falar('restauro')
p1.parar_comer()
p1.falar('restauro')
p1.comer('morango')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
