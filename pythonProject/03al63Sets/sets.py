'''
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda
symmetric_difference ^ (elementos que estao nos dois sets, mas nao em ambos)
set ajuda a eleminar elementos duplicados na lista
sets usando {} ,sets eh como dicionario ,lista usando as {} e so tem valor sem chaves
alem de nao ter chaves nao da para puxar por indice e nescessario iterar para desempacotar
'''

s1 = {1,2,3,4,5}

print(s1)
#{1, 2, 3, 4, 5}
for v in s1:
    print(v)
    #1
    #2
    #3
    #4
    #5

#s2 = {} #quando nao tem valor eh interpretado como um dicionario
s2 = set()#crindo set vazio
s2.add(45)#adiciona
s2.add(67)
s2.add((3,4,5,'daniel'))
print(s2)
#{(3, 4, 5, 'daniel'), 67, 45}
s2.discard((3,4,5,'daniel'))#revome
print(s2)
#{67, 45}
s2.discard(45)
print(s2)
#{67}

s3 = set()
s3.update('Python')#update h parecido com add porem se por uma string ele vai adicionar iterarando
print(s3)
#{'h', 'o', 'n', 't', 'P', 'y'}
#set nao respeita ordem ele se auto organiza
s3.update([1,2,3,4,5], {5,6,7,8})#o elemento 5 vai aparecer so uma vez ele nao aceita
print(s3)
#{1, 2, 3, 4, 't', 'h', 5, 8, 6, 7, 'P', 'y', 'o', 'n'}

s4 = [1,1,1,1,3,3,3,3,3,4, 'daniel', 'daniel']#isso e uma lista elimina elementos duplicados
s4 = set(s4)#damos um cast para set que elimina duplicados
print(s4)
#{'daniel', 1, 3, 4}
s4 = list(s4)#damos um cast para lista novamente
print(s4)
#[1, 3, 4, 'daniel']
print(s4[-1])#acessando ultimo elemento da lista
#daniel

