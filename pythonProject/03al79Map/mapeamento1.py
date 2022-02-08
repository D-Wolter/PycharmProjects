from dados import produtos, pessoas, lista

precos = map(lambda p: p['preco'], produtos)#lambda acessando dicionario
#lambda so funciona pra expressoes
#se preciso somar 5 porcento sem alterar a lista original eh preciso outra funçao
for preco in precos:
    print(preco)
    # 13
    # 55.55
    # 5.5
    # 25
    # 44.5
    # 48
    # 200
    # 130
    # 13
    # 2.9
    #