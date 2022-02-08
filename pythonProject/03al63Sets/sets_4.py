#criamos duas listas com elementos duplicados
l1 = ['luiz', 'joao', 'maria']
l2 = ['luiz', 'joao', 'maria','luiz', 'joao', 'maria','luiz', 'joao', 'maria']

print(l1, l2)
#['luiz', 'joao', 'maria'] ['luiz', 'joao', 'maria', 'luiz', 'joao', 'maria', 'luiz', 'joao', 'maria']
if set(l1) == set(l2):#aqui damos um cast de lista para sets
    print('l1 é igual a l2')
else:
    print('l1 é diferente de l2')

print(l1, l2)#o valores das listas estao inalterados