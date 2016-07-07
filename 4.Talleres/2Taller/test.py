archivo = "test2.in"


for line in open(archivo):
	print line



with open(archivo, 'r') as f:
	read_data = f.read()
	print read_data

read_data = f.read_data