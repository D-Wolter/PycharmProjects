from dados import produtos, pessoas, lista
#codigo igual em lisc comprehension

nova_lista = [x for x in lista if x > 5]

print(list(nova_lista))
#[6, 7, 8, 9, 10]
