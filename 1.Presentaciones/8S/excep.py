nombre = raw_input("ingrese el nombre del archivo, para terminar pulse la tecla q ")


try: 
	file = open(nombre,'r')
	for line in file:
	 	print line.rstrip('\n')
except IOError:
	print "el archivo no existe"
	nombre = raw_input("ingrese el nombre correct, para terminar pulse la tecla q ")
else:
	nombre = raw_input("ingrese el nombre del archivo, para terminar pulse la tecla q ")
	nombre = (nombre).rstrip('\n')
	if nombre == 'q':
		print "chao"