#https://docs.python.org/3/libraty/functions.html#open
#criando dentro do projeto arquivo abc.txt, trabalhar no modo w+ leitura e escrita
file = open('abc.txt', 'w+')

file.write('Linha 1\n')#escrever em file linha 1 e \n quebrar linha
file.write('Linha 2\n')#quando escrevermos e nao salvamos nada executa porque o cursor ja iterou e esta
file.write('Linha 3\n')#no fim do arquivo

file.seek(0, 0)#aqui indicamos que o arquivo deva iniciar no indice 0 absoluto

print('Lendo linhas:')
print(file.read())#le o aquivo inteiro e retorna uma strig
print('###########')

file.seek(0, 0)#como demos um print a iteracao da leitura deve ser iniciada ni indice zero
print(file.readline(), end='')#estamos mandando ler uma linha(no caso linha_1
print(file.readline(), end='')#, end='' por pardrao esse comando quebra uma linha e como ja mandamos
#quebrar a linha, end='' estamos trocando a quebra de linha por nada

file.seek(0, 0)

#print(file.readlines())#comando le todas as linhas

#for linha in file:#podemos escrever assim ou como abaixo
for linha in file.readlines():
    print(linha)

#file.close()# #aqui fechamos o arquivo(nunca deixamos aberto senao da problemas
