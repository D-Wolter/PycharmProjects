# join juntar strings e fazer uma lista

string = ('O brasil é Penta')
print(string)
#O Brasil é Penta
lista = string.split(' ')
print(lista)
#['O', 'brasil', 'é', 'Penta']
string2 = '*'.join(lista)# escolhe o carcter * e join junta tudo numa string
print(string2)
#O*brasil*é*Penta