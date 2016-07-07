import random

size = 10
maxVal= 20

#a = [17, 12, 13, 13, 4, 10, 7, 13, 1, 19]
a = [10,5]

def generateArr(size = 10, maxVal= 20):
	arreglo = []
	for val in range(size):
	  arreglo.append(random.randint(1, maxVal))
	return arreglo

def qsort(arr):

	# Elegir un elemento de la lista: pivote.
	indexPiv = random.randint(0,len(arr))
	pivote = arr[indexPiv]
	print arr, indexPiv, pivote

	# Resituar los demas elementos de la lista a cada lado del pivote,
	izquierda = []
	derecha = []

	for index in range(0,len(arr)):
		item = arr[index]
		if if index != indexPiv
		if item <= pivote :
			#   a un lado queden todos los menores
			izquierda.append(item)
		else:
			#   al otro los mayores
			derecha.append(item)
			#   Los elementos iguales al pivote pueden ser colocados tanto a su derecha como a su izquierda, dependiendo de la implementacion deseada.

	#    !!!! En este momento, el pivote ocupa exactamente el lugar que le correspondera en la lista ordenada.
	# La lista queda separada en dos sublistas
	#     una formada por los elementos a la izquierda del pivote,
	#     y otra por los elementos a su derecha.

		# Repetir este proceso de forma recursiva para cada sublista mientras estas contengan mas de un elemento.
	if(len(arr)>1):
		qsort(izquierda)
		qsort(derecha)
	else:
		return izquierda + derecha

	# Una vez terminado este proceso todos los elementos estaran ordenados.



#qsort(generateArr())
print qsort(a)

