a = [2,2,2,3,3,4,2,2,3,4,0]
b = [2,2,2,2,2,2,2]
c = []
d = [1,1,1,2]

respuesta = [ [2,3], [3,2], [4,1], [2,2], [3,1], [4,1], [0,1]]
rb = [2,7]

def empaquetar(lista):
	i = 0
	while (i < len(lista)):
		cont = 1
		while ((i+cont)<len(lista) and lista[i]==lista[i+cont]):
			cont += 1
		print  lista[i], cont
		i = i + cont


# print a
# print respuesta

empaquetar(a)