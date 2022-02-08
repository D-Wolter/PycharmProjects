"""
while = enquanto
while em python utilizado para realizar acoes enquanto uma condicao for verdadeira.
requisitos: entender condicoes e operadores

#criando um laço de repeticao while ira imprimir todos os numeros abixo de 10
x = 0
while x < 10:
    if x == 3:# pulando o numero 3
        x = x + 1
        continue # ou break que para o processo sem pular para um proximo laço
    print(x)
    x = x + 1
    x += 1 #outra forma de escrever x = x + 1
    #continue #quando o continue eh inserido os codigos abaixo do laço nao serao executados
# poe continue para sair do laco passar a proximo laço ou comando

print('acabou')






coluna = 0
while coluna < 10:
    linha = 0

    while linha < 5:
        print(f'({coluna},{linha})')
        linha += 1

    coluna += 1

print('acabou')

"""
