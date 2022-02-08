# idade = 18
#
# if idade >= 18:
#     print('acesso liberado')
# else:
#     print('proibido para menores')

idade = input('Qual sua idade')

if not idade.isnumeric():
    print('deve digitar apenas numeros')
else:
    idade = int(idade)
    adulto = (idade >= 18)
    msg = "pode Acessar" if adulto else "proibido"

    print(msg)