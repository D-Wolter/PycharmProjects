'''
Fizz Buzz se o parametro da funcao for divisivel por 2, retorne fizz; se o parametro da funcao
for divisivel por 5, retorne buzz, se o parametro da funcao for divisivel por 5 e por 3, retorne
fizzbuzz, caso contrario, retorne o numero enviado
'''

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    if n % 5 == 0:
        return "buzz"
    if n % 3 == 0:
        return "fizz"
    else:
        return n

print(fb(15))