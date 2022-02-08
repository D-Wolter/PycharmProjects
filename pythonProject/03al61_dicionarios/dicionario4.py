#manter um dicionario inalteravel e criando copia para editar
import copy

d1 = {1: 'a', 2: 'b', 3: 'c','d' : ['luiz', 'otavio']}
v = copy.deepcopy(d1)#acessar dicionario dentro de dicionario

v[1] = 'Luiz'
v['d'][0] = 'Joaozinho'

print(d1)
print(v)
#{1: 'a', 2: 'b', 3: 'c', 'd': ['luiz', 'otavio']}
#{1: 'Luiz', 2: 'b', 3: 'c', 'd': ['Joaozinho', 'otavio']}

#deletar uma chave do dicionario
v.pop(1)#deletando chave 1
print(v)
#{2: 'b', 3: 'c', 'd': ['Joaozinho', 'otavio']}

#concatenar dois dicionarios
d2 = {
    'a': 'b',
    'c': 'd',
}
d1.update(d2)
print(d1)
#{1: 'a', 2: 'b', 3: 'c', 'd': ['luiz', 'otavio'], 'a': 'b', 'c': 'd'}