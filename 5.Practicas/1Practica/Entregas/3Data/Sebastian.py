import csv

cantidadArchivos= raw_input("Ingrese la cantidad de archivos a analizar: ")
cantidadEstudiantes=raw_input("Ingrese la cantidad de estudiantes: ")

for a in range(int(cantidadArchivos)):
    deli=' '
    nombreArchivo=raw_input("Ingrese el nombre del archivo : ")
    if ".csv" in nombreArchivo :
        deli=','
    elif ".txt" in nombreArchivo:
        deli=' '
    elif ".ttt" in nombreArchivo:
        deli='-'
    try:
        csvfile= nombreArchivo
        datos=[]
        with open(csvfile,'rb') as csvfile:
            file = csv.reader(csvfile, delimiter=deli, quotechar='|')
            for i in file:
                datos.append(i)
            print datos
            suma=0
            prom=0
            puntajeEstudiante=[]
            for i in range(int(cantidadEstudiantes)):
                for h in range(len(datos[i])):
                    suma= suma+int(datos[i][h])
                    promedio= suma/len(datos)
                puntajeEstudiante.append(suma)
                suma=0
                prom= 0
                #prom=puntajeEstudiante/len(datos)
            print puntajeEstudiante
    except IOError:
            nombreArchivo=raw_input("El nombre del archivo no existe o esta mal escrito, por favor ingreselo nuevamente: ")

            csvfile= nombreArchivo
            datos=[]
            with open(csvfile,'rb') as csvfile:
                file = csv.reader(csvfile, delimiter=deli, quotechar='|')
                for i in file:
                    datos.append(i)
            print datos

            suma=0
            puntajeEstudiante=[]
            for i in range(int(cantidadEstudiantes)):
                for h in range(len(datos[i])):
                    suma= suma+int(datos[i][h])
                puntajeEstudiante.append(suma)
                suma=0
            print puntajeEstudiante