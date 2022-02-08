'''
operadore logicos
and
or
not
in
not in
'''

##comparacao1 and comparacao2
a = 1
b = 2
c = 3
a == b and b < c
#nesse caso as duas sao verdadeiras e volta true



#verdadeiro or verdadeiro uma deve ser verdadeira
a == b or b < c
or se umas das duas for verdadeira# ele retorna true



not a == b and not b < c
not é uma afirmacao inversa
a = 2
b = 3
if not b > a: #not inverteu a expressao abaixo
    print('b é maior que a')
else:
    print('a é maior que b')

#not é muito usado com variaveis vazias ou com zero
a = ""
b = 0
if not a: #se a nao tem valor executar abaixo
    print('por favor preencha o valor de A')

#in vericifa se esta presente alguma caracteristica
nome = "daniel Wolter"
if 'u' in nome: #se a letra u esta em nome print
    print('existe')
else:
    print('nao existe')

#checar usuario e senha
usuario = input('nome do usuario')
senha = input('digite sua senha')

usuario_bd = "Dwolter"
senha_bd = "1234"

if usuario_bd == usuario and senha_bd == senha
    print('voce esta logado')
else:
    print('usuario ou senha invalidas')

