import csv
import numpy as np
import matplotlib.pyplot as plt

files = ["Parcial1.csv","Parcial2.txt","Practica1.csv","Practica2.txt","PracticaFinal.ttt"]
porcentajes = [0.15,0.15,0.2,0.2,0.3]

def getNotaMateria(files):
    evals = []
    for file in files:
        if (".csv" in file):
            delim = ','
        elif(".txt" in file):
            delim = ' '
        elif(".ttt" in file):
            delim = '-'
        evals.append(readNotesEval(file,delim))
    return evals

def readNotesEval(file,delim):
    datos = []
    with open(file, 'rb') as csvfile:
        notas = csv.reader(csvfile, delimiter=delim, quotechar='|')
        for row in notas:
            datos.append(row)
    evals = []
    for j in datos:
        est = []
        for i in range(1,len(j)):
            est.append(int(datos[int(j[0])-1][i]))
        evals.append(est)
    return evals

def getNotaEvaluaciones(evals):
    arr = []
    for eval in evals:
        exa = []
        for est in eval:
            nota = 0
            for i in est:
                nota += i
            exa.append(nota/20.0)
        arr.append(exa)
    return arr

def getNotaFinal(evals):
    notas = np.zeros(len(evals[0]))
    for j in range(0,len(evals)):
        for i in range(0,len(evals[j])):
            notas[i] +=  evals[j][i] * porcentajes[j]
    return notas

def showNotes(arr):
    plt.bar(range(0,len(arr)),arr)
    plt.xlabel('Estudiante')
    plt.ylabel('Notas')
    plt.title('Notas Materia')
    plt.show()

print getNotaFinal(getNotaEvaluaciones(getNotaMateria(files)))
showNotes(getNotaFinal(getNotaEvaluaciones(getNotaMateria(files))))