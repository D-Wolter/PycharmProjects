#https://docs.python.org/3.0/library/datatime.html
#timedelta intervalo de tempo

from datetime import datetime, timedelta
data = datetime(2019, 4, 20, 10, 56, 20)
print(data)
#2019-04-20 10:56:20

print(data.strftime('%d/%m/%Y %H:%M:%S'))
#20/04/2019 10:56:20

data2 = datetime.strptime('04/03/1981', '%d/%m/%Y')
print(data2)

data3 = datetime.strptime('04/03/1981 17:00:00', '%d/%m/%Y %H:%M:%S')
data3 = data3 + timedelta(days=5, hours=10)
print(data3.strftime('%d/%m/%Y %H:%M:%S'))
#10/03/1981 03:00:00

d1 = datetime.strptime('04/03/2019 17:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('10/03/2019 09:00:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)
#5 days, 16:00:00