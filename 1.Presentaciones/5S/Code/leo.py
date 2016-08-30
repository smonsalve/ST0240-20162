archivo1 = "Entrada1.in"
archivo2 = "Entrada2.in"
archivo3 = "Entrada3.in"


f = open(archivo1, "rb")

arreglo = []

for item in f:
    a = item.rstrip()
    arreglo.append(a)

print arreglo


