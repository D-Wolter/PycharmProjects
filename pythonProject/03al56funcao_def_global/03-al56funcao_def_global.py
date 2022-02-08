
variavel = 'valor'

def func():
    for v in variavel:
        return v

def func2():
    global variavel# global trona a variavel para escopo global(mas nao devemos escrever assim
    
    variavel = ' outro valor'
    print(variavel)

func()
variavel = 'valor'

def func():
    for v in variavel:
        return v

def func2():
    global variavel# global trona a variavel para escopo global(mas nao devemos escrever assim

    variavel = ' outro valor'
    print(variavel)

func()
func2()

print(variavel)
func2()

print(variavel)