import sys
import time

l1 = [x for x in range(100)]#salva todos valores na memoria
l2 = (x for x in range(100))#dessa forma fica comprimido sem alocar muito espaco

print(sys.getsizeof(l1))#8448728
print(sys.getsizeof(l2))#112

for v in l2:
    print(v)