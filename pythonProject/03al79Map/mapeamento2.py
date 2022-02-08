from dados import produtos, pessoas, lista

def aumenta_preco(p):
#    p['preco'] = p['preco'] * 1.05#adicionando 5 porcento
    p['preco'] = round(p['preco'] * 1.05, 2)#cod acima mais round e 2 no fim pra duas casas decimais
    return p

precos_juros = map(aumenta_preco, produtos)

for produto in precos_juros:
    print(produto)
    # {'nome': 'p1', 'preco': 13.65}
    # {'nome': 'p2', 'preco': 58.28}
    # {'nome': 'p3', 'preco': 5.78}
    # {'nome': 'p4', 'preco': 26.25}
    # {'nome': 'p5', 'preco': 46.73}
    # {'nome': 'p6', 'preco': 50.4}
    # {'nome': 'p7', 'preco': 210.0}
    # {'nome': 'p8', 'preco': 136.5}
    # {'nome': 'p9', 'preco': 13.65}
    # {'nome': 'p10', 'preco': 3.04}
    #