#https://docs.python.org/3/libraty/functions.html#open
#melhor modo pythonico de ler

#  a+ ativao append mode, adicionar sem apagar nada
# a poe o cursor no final do arquivo e + adiciona
with open('abc.txt', 'a+') as file:
    file.write('Outra linha')#adicionamos
    file.seek(0)#começar indice zero
    print(file.read())
