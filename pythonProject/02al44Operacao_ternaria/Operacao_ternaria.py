#sistema login
# logged_user = False
#
# if logged_user:
#     msg = "usuario logado"
# else:
#     msg = "nescessario logar"
# print(msg)

#cod parecido mais siplificado
logged_user = False
#msg = 'usuario logado' if logged_user else "precisa logar."
msg = 'usuario logado' if (logged_user == True) else "precisa logar."
print(msg)