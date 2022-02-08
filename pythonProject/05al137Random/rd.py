import random
import string

# Gera um número inteiro entra A e B
# inteiro = random.randint(10, 20)

# Gera um número de ponto flutuante entra A e B
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0.0 e 1.0
flutuante = random.random()

# Gerar um número aleatório usando a função range()
#                          de    ate   pulando de 10
inteiro = random.randrange(900, 1000, 10)



lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista, 2) ##sorteia dois nomes diferentes aleatorios por vez
# sorteio = random.choices(lista, k=2) #sorteia dois nomes aleatorios por vez porem pode repetir o mesmo nome
# sorteio = random.choice(lista) #sorteia um nome na lista

# Embaralha a lista
random.shuffle(lista)# embaralhar a lista

# Gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
