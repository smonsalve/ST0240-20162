

def getnotas(notas_est):
    try:
        notas_estudiante = open(notas_est, 'r+')
        print notas_estudiante.read()
    except(IOError):
        print "no se encontro el archivo\n"


elarchivo = open("Nombres.txt","r+")
for line in elarchivo:
    getnotas(line.rstrip())
