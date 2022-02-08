'''
Pilhas e filas

Pilha (stack) - LIFO - last in, first out.
exemplo: pilha de livros que sao adicionados um sobre o outro

Fila (queue) - FITO - first in, first out.
exemplo: uma fila de banco, filas podem ter efeitos colaterais em desepenho, porque cada item alterado, todos
os indices serao modificados.
'''

livros = list()
livros.append('amor')
livros.append('ilusao')
livros.append('romance')
livros.append('poesia')
livros.append('suspense')
print(livros)
livro_removido = livros.pop()
print(livros, livro_removido)
# ['amor', 'ilusao', 'romance', 'poesia', 'suspense']
# ['amor', 'ilusao', 'romance', 'poesia'] suspense

livro_removido = livros.pop()
livro_removido = livros.pop()
livro_removido = livros.pop()
livro_removido = livros.pop()
print(livros, livro_removido)

from collections import deque
from time import sleep
fila = deque()
fila.append('amor')
fila.append('ilusao')
fila.append('romance')
fila.append('poesia')
fila.append('suspense')
fila.popleft()#pop() retira a direita, popleft() retira da esquerdA
for nome in fila:
    print(nome)
    # amor
    # ilusao
    # romance
    # poesia
    # suspense

espera = deque(maxlen=5)
espera.extend(['daniel','tiago','luana','gabriel'])
#.extend() insere lista a direita, extedleft() isere lista a esquerda
print(espera)
espera.append('marina')
#append() adiciona um item a direita, appendleft() adiciona um item a esquerda
print(espera)
espera.append('clara')
print(espera)
# deque(['daniel', 'tiago', 'luana', 'gabriel'], maxlen=5)
# deque(['daniel', 'tiago', 'luana', 'gabriel', 'marina'], maxlen=5)
# deque(['tiago', 'luana', 'gabriel', 'marina', 'clara'], maxlen=5)

sala_espera = deque(maxlen=6)

for i in range(20):
    sala_espera.append(i)
    #sleep(1)
    print(sala_espera)
    # deque([0], maxlen=6)
    # deque([0, 1], maxlen=6)
    # deque([0, 1, 2], maxlen=6)
    # deque([0, 1, 2, 3], maxlen=6)
    # deque([0, 1, 2, 3, 4], maxlen=6)
    # deque([0, 1, 2, 3, 4, 5], maxlen=6)
    # deque([1, 2, 3, 4, 5, 6], maxlen=6)
    # deque([2, 3, 4, 5, 6, 7], maxlen=6)
    # deque([3, 4, 5, 6, 7, 8], maxlen=6)
    # deque([4, 5, 6, 7, 8, 9], maxlen=6)
    # deque([5, 6, 7, 8, 9, 10], maxlen=6)
    # deque([6, 7, 8, 9, 10, 11], maxlen=6)
    # deque([7, 8, 9, 10, 11, 12], maxlen=6)
    # deque([8, 9, 10, 11, 12, 13], maxlen=6)
    # deque([9, 10, 11, 12, 13, 14], maxlen=6)
    # deque([10, 11, 12, 13, 14, 15], maxlen=6)
    # deque([11, 12, 13, 14, 15, 16], maxlen=6)
    # deque([12, 13, 14, 15, 16, 17], maxlen=6)
    # deque([13, 14, 15, 16, 17, 18], maxlen=6)
    # deque([14, 15, 16, 17, 18, 19], maxlen=6)
    #


PARTICIPANTES = deque(maxlen=10)
PARTICIPANTES.extend([1,2,3,4,5,6])
print(PARTICIPANTES)
PARTICIPANTES.insert(2, 'Daniel')
print(PARTICIPANTES)
# deque([1, 2, 3, 4, 5, 6], maxlen=10)
# deque([1, 2, 'Daniel', 3, 4, 5, 6], maxlen=10)
print(PARTICIPANTES.index('Daniel'))#exibir numero indice
#2
print(PARTICIPANTES.count('Daniel'))#conta quantas veses repete
#1
PARTICIPANTES.reverse()#inverte a ordem
print(PARTICIPANTES)
#deque([6, 5, 4, 3, 'Daniel', 2, 1], maxlen=10)