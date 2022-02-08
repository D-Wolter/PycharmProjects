
l1 = ['luiz', 'joao', 'maria']
l2 = ['luiz', 'joao', 'maria','luiz', 'joao', 'maria','luiz', 'joao', 'maria']

print(l1 != l2)# l1 eh diferentes de l2
#True

l1 = set(l1)
l2 = set(l2)

print(l1 == l2)
#True

