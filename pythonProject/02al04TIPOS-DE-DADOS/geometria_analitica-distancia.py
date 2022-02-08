import math


# função que permite calcular a distância
# entre dois pontos no plano (R2)
def distancia2d(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return c


# função principal do programa
def main():
    # vamos ler os dados do primeiro ponto
    x1 = float(input("Informe o x do primeiro ponto: "))
    y1 = float(input("Informe o y do primeiro ponto: "))

    # vamos ler os dados do segundo ponto
    x2 = float(input("Informe o x do segundo ponto: "))
    y2 = float(input("Informe o y do segundo ponto: "))

    # vamos obter a distância entre eles
    distancia = distancia2d(x1, y1, x2, y2)
    print("Distância entre os dois pontos: %0.2f" % distancia);


if __name__ == "__main__":
    main()