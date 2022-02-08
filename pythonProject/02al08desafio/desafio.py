"""
* criar variaveis para nome (str, idade (int),
*altura (float) e peso (float) de uma pessoa
*criar variavel com o nascimento da pessoa (baseado na idade e no ano atual)
*obter i imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
*exibir um texto com todos os valores na tela usando f-strings (com as chaves)
"""

nome = 'Daniel'
idade = 40
peso = 70.5
altura = 1.70
imc = peso / (altura *altura)
data_atual = 2021
nasc = data_atual - idade

print('{} tem {} anos, {} de altura e pesa {:.0f}kg.'.format(nome, idade,altura,peso))
print('O IMC de {} é {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, nasc))#meu codigo

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nasc}.')# cod do prof