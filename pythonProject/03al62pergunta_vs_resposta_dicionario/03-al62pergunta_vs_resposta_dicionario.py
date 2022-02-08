print()
print('Texto explicativo')

perguntas = {#lista possui 3 camadas
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'respostas': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}
print()#esta apenas criando uma linha de espaço da execuçao

respostas_certas = 0#fazendo contagem de acertos
for pergunta, dados_pergunta in perguntas.items():#iterar chave e valor .items
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')#f' comecçou com aspas siples string deve ter a dupla para funcionar

    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')#iterando depois de desempacotar acima

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('EHHHHHH!!! Você acertou!!!!')
        respostas_certas += 1
    else:
        print('IXXIIIII!!! Você ERROU!!!!')

    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')