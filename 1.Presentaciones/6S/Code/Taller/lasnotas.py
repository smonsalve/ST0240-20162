

def getnotas(notas_est):
    notas_estudiante = open(notas_est, 'r+')
    print notas_estudiante.read

elarchivo = open("Nombres.txt","r+")
for line in elarchivo:
    getnotas(line.rstrip())



