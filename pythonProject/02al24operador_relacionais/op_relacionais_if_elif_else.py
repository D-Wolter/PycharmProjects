"""
operadores relacionais servem para comparar coisas
todas as vezes que sao usados retorna um valor bolleado true or false
== checar a igualdade
> checar se maior
>= checar se maior ou igual
<
<=
!= se é diferente
"""
#num_1 = 2
#num_2 = 2
#expresao = (num_1 > num_2) #comando compara as partes
#print(expresao)

nome = input('qual seu nome? ')
idade = input('1qual sua idade? ')
idade = int(idade) #converter input (str) para INT

idade_minima = 18
idade_maxima = 45


if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} pode pegar emprestimo.')
else:
    print(f'{nome} BLOQUEADO')