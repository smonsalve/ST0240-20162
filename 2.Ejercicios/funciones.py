nombre = "Bruce Wayne"

delincuentes = 13
eliminados = 3
nacidos = 2

print ("Buenas Tardes")
print (nombre)

def agregarDelincuentes(cantidad):
	nuevosDelincuentes = delincuentes + cantidad
	return nuevosDelincuentes

def disminuirVariable(variable, cantidad):
	return variable - cantidad

print ("Antier habia {0} delincuentes en ciudad Gotica").format(delincuentes)
print ("ayer nacieron {0} y se eliminaron {1}").format(nacidos, eliminados)

delincuentes = agregarDelincuentes(nacidos)
delincuentes = disminuirVariable(delincuentes, eliminados)

print ("hoy hay {0} en ciudad Gotica").format(delincuentes)