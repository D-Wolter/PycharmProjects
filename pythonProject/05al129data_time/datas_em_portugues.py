
#data atual

from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays
dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
setlocale(LC_ALL, 'pt_BR.utf-8')

print(mdays)
#[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]quantidade de dias de cada mes

formatacao1 = dt.strftime('%A, %d de %B de %Y as %H:%M:%S horas')
#terça, 27 de julho de 2021

formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
#27/07/2021 14:51:27

print(formatacao2)

print(mes_atual, mdays[mes_atual])
#7 31