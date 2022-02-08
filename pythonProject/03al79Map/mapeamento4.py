from dados import produtos, pessoas, lista
#lista todas pessoa em pessoas

def idade_callback(p):#criando novo valor idade para callback(cria nova lista
    p['callback_idade'] = p['idade'] + 4
    return p

idades = map (idade_callback, pessoas)

for pessoa in idades:#listar por idade
    print(pessoa)