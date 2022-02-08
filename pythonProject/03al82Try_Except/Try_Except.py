#sempre no python trabalha com try e except, porem o cod para
#se chamar a funcao try ele pode apenas tentar executar o cod se encontra erro
#retornar except, e vc tratar o erro.
3

try:#se nao tiver erro cai no else
    a =[]
    b ={}
#    print(a[1])#indice 1 nao existe
#   print(b[1])#indice nao existe
#except:                #except detecta todos os erros
#    print('erro')
except NameError as erro:#nomeando o tipo de erro
    print('tratar erro', erro)
except (IndexError, KeyError) as erro:
    print('erro de indice ou chave')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:#sera executado se o try nao tiver nenhum erro
    print('Seu cod foi executado com sucesso')
    print(a)
finally:#sempre eh executada idependentete de ter erro ou estar correto
    print('numero de protocolo gerado')
    
print('aqui continua o cod')