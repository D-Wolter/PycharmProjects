#https://docs.python.org/3/libraty/exceptions.html

def divide(n1, n2):
    try:#levantando execoes (se o try: for usado fora do escopo global vc nao interfere
# na linguagem, criando como acima vc pode a cada erro gerar ualgo para corrigir erros
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise#encaminha para o  except

try:
    print(divide(2, 0))
except:
    print('errro')