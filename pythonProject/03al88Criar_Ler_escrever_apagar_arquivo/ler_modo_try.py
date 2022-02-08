#https://docs.python.org/3/libraty/functions.html#open
#costumase usar o bloco try para abrir arquivos

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')# o arquivo esta vazio entao escrevemos
    file.seek(0)
    print(file.read())
finally:              #para garantir que o arquivo sera fechado se holver erro
    file.close()

