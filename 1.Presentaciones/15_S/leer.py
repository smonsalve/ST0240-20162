class Evaluacion:

	def __init__(self,name, percen, presentaron, totalPun, noPre, pp):
		self.nombreEv  = name
		self.porcentaje = percen
		self.presentaron = presentaron
		self.totalPuntos =  totalPun
		self.noPresentaron = noPre
		self.porcentajePuntos =  pp
		self.notas = ""

	def __str__(self):
		to_string = self.nombreEv + " " + self.porcentaje + " " + self.totalPuntos  + " " + self.noPresentaron + " " + self.porcentajePuntos + "\n" + self.notas
		return to_string

	def asignarNotas(self):
		archivo = open(self.nombreEv,'r')
		lasnotas = ""
		for item in archivo:
			lasnotas += item
		self.notas = lasnotas


indice = "Indice.txt"
archivo = open(indice,'r')

archivos = int(archivo.readline()[22:])
estudiantes = int(archivo.readline()[21:])

evals = []
for evs in range(archivos):
	archivo.readline()
	nombreEv = archivo.readline().rstrip('\n')
	porcentaje = archivo.readline()[29:]
	presentaron = archivo.readline()[13:]
	totPuntos = archivo.readline()[14:]
	noPre = archivo.readline().rstrip('\n')
	ppuntos = archivo.readline().rstrip('\n')
	ev = Evaluacion(nombreEv,porcentaje,presentaron,totPuntos,noPre,ppuntos)
	ev.asignarNotas()
	evals.append(ev)
	print ev
