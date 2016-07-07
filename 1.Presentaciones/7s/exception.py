cantidad = int(input("ingrese cantidad de valores a ingresar"))
int(input("ingrese valores"))

input()
(x,y) = (5,0)

try:
	z = x/y
except ZeroDivisionError:
	print "division por cero"
else:
	print "todo Bien!"