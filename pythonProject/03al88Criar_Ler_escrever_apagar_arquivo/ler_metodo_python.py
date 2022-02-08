#https://docs.python.org/3/libraty/functions.html#open
#melhor modo pythonico de ler

#gerenciador de contexto nao precisa mandar fechar o arquivo
# #open eh uma funcao e file a variavel da funcao

with open('abc.txt', 'r') as file:
    print(file.read())
