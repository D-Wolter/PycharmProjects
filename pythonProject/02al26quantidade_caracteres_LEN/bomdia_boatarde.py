horario = input('que horas sao de 0-23')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('horario de ser de 0 a 23')
    else:
        if horario <= 11:
           print('bom dia')
        elif horario <= 17:
            print('boa tarde')
        else:
            print('boa noite')

else:
    print('digite um horariocom numeros')