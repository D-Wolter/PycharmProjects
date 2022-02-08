'''
Listas em Python
fatiamento
append, insert, pop, del clear, extend, +
min, max
range
'''
#indice     0         1          2         3       4     5     6
#indice-    7         6          5         4       3     2     1
cliente = ['Daniel', 'Wolter', 'Martins', 40, 1.87, True]
profisao = ['restaurador', 'programador']
lista2 = ['Daniel', 'Wolter', 'Martins', 40, 1.87, True]
string = 'Daniel Wolter Martins'
cliente.append('Sangue O+')# adiciona a lista algo e fica iteravel
cliente.insert(0, "Masculino")#adiciona no indice 0 a informacao

#dados_completos = cliente + profisao
cliente.extend(profisao)# profissao virou extend de cliente
#cliente.pop()#pop apaguaria a ultima casa da lista
#del(cliente[0:3])#esse comando apagaria do indice zero ao 3 da lista cliente
print(cliente)

print(cliente[0:4])
print(profisao)