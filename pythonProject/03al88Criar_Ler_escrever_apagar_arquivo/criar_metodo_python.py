#https://docs.python.org/3/libraty/functions.html#open
#melhor modo pythonico de criar

#gerenciador de contexto nao precisa mandar fechar o arquivo
with open('abc.txt', 'w+') as file:#open eh uma funcao e file a variavel da funcao
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())
