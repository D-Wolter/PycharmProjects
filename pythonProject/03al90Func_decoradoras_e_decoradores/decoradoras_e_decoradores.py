def master(funcao):
    def slave(*args, **kwargs):
        print('agora estou decorada')
        funcao(*args, **kwargs)
    return slave

# funcao decoradora
@master  #esse é um decorador
def fala_oi():
    print('oi')

#fala_oi = master(fala_oi)
#fala_oi()

@master
def outra_funcao(msg):
    print(msg)

outra_funcao('ola sou daniel')
