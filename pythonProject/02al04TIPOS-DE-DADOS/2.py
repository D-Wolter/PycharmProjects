from math import hypot
import emoji

# --------------------------------------------------------------------------

c_oposto = float(input('Digite a medida do cateto oposto: '))
c_adjacente = float(input('Digite a medida do cateto adjancente: '))
hipotenusa = (c_adjacente ** 2 + c_oposto ** 2) ** (1 /
                                                    2)

print(f'O cateto oposto mede {c_oposto} \n'
      f'O cateto adjacente mede {c_adjacente} \n'
      f'E a hipotenusa é {hipotenusa:.2f} \n\n'
      f'Fim do programa.')

# --------------------------------------------------------------------------

print(f"\n\n\033[1;91m'☼☼☼☼☼☼☼☼☼☼ Catetos e hipotenusa ☼☼☼☼☼☼☼☼☼☼'\033[m\n")

cat_oposto = float(input('Qual o comprimento do cateto oposto? '))
cat_adjacente = float(input('Comprimento do cateto adjacente? '))

# a hipotenusa é a raiz quadrada da soma dos quadrados dos catetos
hipotenusa = (cat_oposto ** 2 + cat_adjacente ** 2) ** (1 / 2)

print(f'\nO cateto oposto mede {cat_oposto}\n'
      f'O cateto adjacente mede {cat_adjacente}\n'
      f'A hipotenusa é {hipotenusa:.2f}')

# --------------------------------------------------------------------------

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

# hi = (co ** 2 + ca ** 2) ** (1 / 2) # fórmula para calculo da hipotenusa
# a hipotenusa é a raiz quadrada da soma dos quadrados dos catetos
# aqui foi importado o metodo hypot para calcular a hipotenusa

hipotenusa = hypot(cateto_oposto, cateto_adjacente)  # usando ''from math import hypot''
print(emoji.emojize(f'A hipoenusa vai medir: {hipotenusa:.2f}\n\n'))
