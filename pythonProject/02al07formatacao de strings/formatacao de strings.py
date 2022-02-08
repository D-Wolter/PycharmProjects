nome = 'Daniel Wolter'
idade = 32 # int
altura = 1.80 # float
e_maior = idade > 18 #bool
datA_1 = False #bool
data_atual = 2019
peso = 80
imc = peso/ (altura * altura)

print(idade * altura)
print(nome, 'tem', idade, "anos de idade e deu imc é", imc)
#Daniel Wolter tem 32 anos de idade e seu imc é 24.691358024691358
#f string simplifica a escrita
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')
#Daniel Wolter tem 32 anos de idade e seu imc é 24.691358024691358

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')#.2f determina quantas casa exibi depois do ponto
#Daniel Wolter tem 32 anos de idade e seu imc é 24.69

print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
#Daniel Wolter tem 32 anos de idade e seu imc é 24.691358024691358
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
#Daniel Wolter tem 32 anos de idade e seu imc é 24.69
print('{2} tem {1} anos e seu imc é {0}'.format(nome, idade, imc))
#podese enumerar as casa e mudar de ordem respeitando o format
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
#criando variaveis dno format