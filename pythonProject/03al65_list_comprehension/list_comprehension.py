
l1 = [1,2,3,4,5,6,7,8,9]

ex1 = [variavel for variavel in l1]#exiba cada variavel para as variaveis de l1
#print(ex1)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

ex2 = [v *2 for v in l1]#valor multiplicado por 2 em cada valor em l1
#print(ex2)
#[2, 4, 6, 8, 10, 12, 14, 16, 18]

ex3 = [(v, v2) for v in l1 for v2 in range(3)]#para cada elemento crianr uma tupla de contagem ate 3
#print(ex3)
#[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]


l2 = ['luiz', 'mauro', 'maria']
ex4 = [v.replace('a', '@').upper() for v in l2]#valor repassar a por @ e por em caixa alta valores em l2
#print(ex4)
#['LUIZ', 'M@URO', 'M@RI@']

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]#inverte o valor e depois a chave

ex5 = dict(ex5)#tranforma a tupla em um dicionario
#{'chave', 'valor', 'chave2', 'valor2'}

l3 = list(range(100))#criando uma lista com 100 valoresin range
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]#separar todos od numeros que sao divisiveis por 3 e 8
#print(ex6)
#[0, 24, 48, 72, 96]

ex7 = [v if v % 3 == 0 else 'nao é' for v in l3]#se valor nao for divisivel por 3 vai usar valor nao é nos vaolres l3
print(ex7)
