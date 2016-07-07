cantidad = int(input("imprima la cantidad de datos a ingresar:"))
datos = []

for i in range(0,cantidad):
		val = input(("ingrese valor #{}: ").format(i))
		datos.append(int(val))

print datos