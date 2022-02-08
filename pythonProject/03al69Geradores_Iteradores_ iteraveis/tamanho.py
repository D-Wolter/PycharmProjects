'''
import sys
lista = list(range(100000))

print(sys.getsizeof(lista))
#800056 consumindo bites a lista acima aloca cada valor do range
'''

import sys
import time

def gera():
    r = []#cria um array em branco
    for n in range(100):#iteracao com range de 0 a 100
        r.append(n)
        time.sleep(0.1)#python leg 0.1 segundo
    return r
g = gera()

for v in g:
    print(v)