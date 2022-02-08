'''
formatando valores com modificadores

:s - texto - string
:d - inteiros - int
:f - numeros ponto flutuante - float
:.(numero)f - quantidade de dasas decimais - float
:(caractere) (> ou < ^) (quantidade) (tipos - s, d ou f)

> - esquerda
< - direita
^ - centro
'''

#:.(numero)f - quantidade de dasas decimais - float
#vamos fazer duas variaveis e uma divisao com numero flutuante extenso
#num1 = 10
#num2 = 3
#divisao = num1 / num2
#print(divisao)
#vamos limitar as casas decimais
#print (  '{:.2f}'.format(divisao)  )# format dois pontos chama funcao formatacao,
#.2 seria duas casas decimais, f porque a variante virou ponto flutuante
#print( f'{divisao:.2f}')# f strigs escreve a mesma funcao

#:d - inteiros - int

#:(caractere) (> ou < ^) (quantidade) (tipos - s, d ou f)
#determinar um tamanho padrao e tauvez completar com zero ou espaço
num1 = 325
# se vc quiser deterinar 10 casa decimais e completar zeros a esquerda
print(f'{num1:0>10}')
#chama f string poe a variavel na chave, : chama funcao, 0 o digito que desejo ser
#inserdo no campo vazio, > quero que fique a esquerda, 10 determina o numero de casas
nome = 'Daniel Wolter'
print(f'{nome: ^20}')

#:f - numeros ponto flutuante - float
#por casas decimais em numeros inteiros
print(f'{num1:.2f}')# vamos pegar o numero inteiro e adicionar .00 e tranformar em float
print(f'{num1:0>10.2f}')#aqui adicionamos zeros a esquerda p ficar padrao 10 casas

#:s - texto - string
print(f'{nome:#^50}')#{ variavel, : chama funcao, # completa com digito, ^ centraliza
#50 determina casas decimais
print(nome.lower())# minusculo
print(nome.upper())#maiussculo
print(nome.title())# primerias letras maiusculo