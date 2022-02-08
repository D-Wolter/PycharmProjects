string = ('O Brasil é o país do Futebol, o brasil é penta')
lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista2:# repara que na segunda linha tem um espaço e letra min
    print(valor)
    #O Brasil é o país do Futebol
    # o brasil é penta
    print(valor.strip())  # strip remove espaço do inicio e do fim da string
    #O Brasil é o país do Futebol
    #o brasil é penta
    print(valor.strip().capitalize())  # capitalize poe a primeira letra em maiusculo(upper deixa todas maiusculas)
    # O Brasil é o país do Futebol
    # O brasil é penta

for valor in lista1:
    print(valor)
    # o
    # país
    # do
    # Futebol,
    # o
    # brasil
    # é
    # penta
    #