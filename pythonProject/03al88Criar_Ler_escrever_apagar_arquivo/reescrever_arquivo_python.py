#https://docs.python.org/3/libraty/functions.html#open
#melhor modo pythonico reescrever arquivo

#  w+ reescreve o arquivo
with open('abc.txt', 'w+') as file:
    file.write('Outra linha')#adicionamos
    file.seek(0)#começar indice zero
    print(file.read())
