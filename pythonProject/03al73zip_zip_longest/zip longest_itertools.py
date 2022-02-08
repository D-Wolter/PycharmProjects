
from itertools import zip_longest, count

indice = count()
cidades = ['sao paulo', 'belo horizonte', 'salvador', 'monte belo', 'outra']
estados = ['sp', 'mg', 'ba']
#executou zip longest que uniu inclusive a quarta opcao e retorno none

cidades_estados = zip(indice, estados, cidades)#define valor padrao onde falta
#print(list(cidades_estados))
#[('sp', 'sao paulo'), ('mg', 'belo horizonte'), ('ba', 'salvador'), ('estado', 'monte belo'), ('estado', 'outra')]

for valor in cidades_estados:
    print(valor)
    # (0, 'sp', 'sao paulo')
    # (1, 'mg', 'belo horizonte')
    # (2, 'ba', 'salvador')
