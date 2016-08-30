

def getnotas(notas_est):
    cont = []
    try:
        notas_estudiante = open(notas_est, 'r+')
        cont = notas_estudiante.read()
    except(IOError):
        print "no se encontro el archivo"
        cont = [0,0,0]
    return cont

est = {}

elarchivo = open("Nombres.txt","r+")

o = []
for line in elarchivo:
    o = getnotas(line.rstrip())
    est[o[0]]=o[1]

print est
