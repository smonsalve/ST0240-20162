import sys
import csv

def abrir_csv(doc):
    with open(doc) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for line in entrada:
            print line


def abrir_txt(txt):
    archivo = open(txt, "r")
    contenido = archivo.read()
    print contenido

def abrir_archivo(doc):
    try:
        file = open(doc, "r")
        for line in file:
            print (line.rstrip('\n'))
    except IOError:
        doc = raw_input("No fue posible encontrar el archivo, por favor intente de nuevo")
        return introdusca

a = 'Sistema de notas de la materia Programacion de computadores\n'
a += 'Seleccione una de las siguientes opciones:\n'
a += '1- Ingrese la cantidad de archivos\n'
a += '2- Ingrese cantidad total de estudiantes\n'
a += '3- Ingrese los nombres de los archivos\n'
a += '4- Salir\n'
a += 'Seleccione una opcion'

introdusca = input(a)

for i in a:
    if introdusca <= 4:
        if introdusca == 1:
            input('Cuantos archivos desea analizar?')
        elif introdusca == 2:
            input('Cuantos estudiantes va a analizar?')
            break
        elif introdusca == 3:
            documento = raw_input('Que archivos desea abrir?')
            abrir_archivo(documento)
            break
        elif introdusca == 4:
            print 'Hasta luego'
            sys.exit(4)
    elif introdusca > 4:
        print 'Opcion invalida'
        introdusca = input('Intentelo otra vez')

def porcentajes():
    file = documento

indice = raw_input('Ingrese el indice')
abrir_txt(indice)