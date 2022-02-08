#aqui estamos puxando o outro arquivo do diretorio (arquivo python dados)
#importando as listas: produtos, pessoas, lista

from dados import produtos, pessoas, lista

#importando valores da lista do outro arquivo dados
nova_lista = map(lambda x: x*2, lista)#multiplica valores da lista numa nova_lista
#chamando funcao map, que como primeiro argumento deve ter uma funcao no caso lambda
print(lista)
print(list(nova_lista))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]