nome = input('digite seu nome')
tamanho = len(nome)#conta quantos caracteres

if tamanho <= 4:
    print('curto')
elif tamanho <= 6:
    print('normal')
else:
    print('grande')