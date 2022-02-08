
def func(*args):
    args = list(args)#args trabalha com tupls que nao aceita alterar o valor entao faz um cast para list
    args[0] = 20
    print(args)

func(1,2,3,4,5)
#[20, 2, 3, 4, 5]