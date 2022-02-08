# funcao atrasa o tempo da funcao e conta o tempo

from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        star_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - star_time) * 1000
        print(f'\nA Funcao {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(100):
        print(i, end='')
        #sleep(1)

demora()
#0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899
#A Funcao demora levou 0.98ms para executar.
