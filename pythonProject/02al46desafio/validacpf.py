"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# Loop infinito
while True:
    cpf_and_digito = '04045683941'
    #cpf_and_digito = input('Digite um CPF: ')
    cpf_sem_digito = cpf_and_digito[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    reverso_soma = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        reverso_soma += int(cpf_sem_digito[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            dig_seg = 11 - (reverso_soma % 11)

            if dig_seg > 9:                   # Se o digito for > que 9 o valor é 0
                dig_seg = 0
            reverso_soma = 0                   # Zera o total
            cpf_sem_digito += str(dig_seg)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = cpf_sem_digito == str(cpf_sem_digito[0]) * len(cpf_and_digito)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf_and_digito == cpf_sem_digito and not sequencia:
        print('Válido')
    else:
        print('Inválido')
