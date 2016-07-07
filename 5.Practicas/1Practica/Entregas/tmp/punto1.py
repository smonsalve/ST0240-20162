def getFileName():
	nombreArchivo = raw_input("Ingrese el nombre del archivo: ")
	return nombreArchivo

def getArchivos(cadena):
	archivos = -1
	if ("Cantidad de Archivos" in cadena):
		archivos =  int(cadena[cadena.index(":")+1:])
	return archivos

def getEstudiantes(cadena):
	estudiantes = -1
	if ("Estudiantes totales" in cadena):
		estudiantes = int(cadena[cadena.index(":")+1:])
	return estudiantes

def leerArchivo(nombreArchivo):
	try:
		file = open(nombreArchivo,'r')
	except IOError:
		print "Nombre del Archivo Invalido, intente nuevamente\n\n "
		leerArchivo(getFileName())
	return file

def procesarArchivo(file):
	evals = []
	data = {'archivos':0, 'estudiantes':0, 'evals': evals}
	case = 0
	s = 0

	for line in file:
		if(case==0):
			data['archivos'] =  getArchivos(line)
			case = 1
		elif(case==1):
			data['estudiantes'] = getEstudiantes(line)
			case = 2
		elif(case==2):
			result = procesarEvaluacion(evals,line.rstrip('\n'),s)
			s = result[1]
			evals.append(result[0])
		elif(case == -1):
			print "El Error"
	return data

def getNombreEval(cadena):
	nombreEval = ""
	if ( (".csv" in cadena) or (".txt" in cadena) or (".ttt" in cadena) ):
		nombreEval = cadena.rstrip('\n')
	return nombreEval

def getTotalPuntos(cadena):
	puntos = -1
	if ("Total Puntos" in cadena):
		puntos = int(cadena[cadena.index(":")+1:])
	return puntos

def getPresentaron(cadena):
	presentaron = -1
	if ("Presentaron" in cadena):
		presentaron = int(cadena[cadena.index(":")+1:])
	return presentaron

def procesarEvaluacion(evaluacion,cadena,stage):
	if(stage == 0):
		nom = getNombreEval(cadena)
		if(nom != ""):
			evaluacion.append(nom)
			stage = 1
	elif(stage == 1):
		pres = getPresentaron(cadena)
		if (pres != -1 ):
			evaluacion.append(pres)
			stage = 2
	elif(stage == 2):
		evaluacion.append(getTotalPuntos(cadena))
		stage = 3
	return (evaluacion,stage)

nombreIndice = "Indice.txt"
print procesarArchivo(leerArchivo(nombreIndice))
#leerArchivo(getFileName())
