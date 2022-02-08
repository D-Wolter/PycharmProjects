# contador
'''
alunos = 50

while alunos <= 100:
    print(alunos)
    alunos += 1
'''
#acumulador

alunos = 1
acumulador = 1

while alunos <= 10:
    print(alunos, acumulador)

    acumulador = acumulador + alunos
    alunos += 1
else:
    print('terminou o laço')