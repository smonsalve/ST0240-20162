import numpy as np
import math
import re
import matplotlib.pyplot as plt
import matplotlib.path as mpath
z = 1
while(z == 1):
    print("Se*or usuario, por favor ingrese la ubicaci*n del archivo *ndice, a continuaci*n, ingrese la ubicaci*n de los documentos restantes. ")
    j = 0
    def getFileName(j):
        if(j == 0):
            message = "\n" + "Por favor ingrese la ruta de su archivo: "
        else:
            if(j == math.sqrt(3)):
                message = "Se*or usuario, uno de los porcentajes en el archivo *ndice tiene un problema, por favor corrija lo e ingrese nuevamemente la ruta completa del archivo: "
            else:
                if(j == math.sqrt(2)):
                    message = "Se*or usuario, su archivo est* vac*o, por favor intente con uno que s* tenga contenido: "
                else:
                    if(j == math.sqrt(5)):
                        message = "Se*or usuario, la cantidad de estudiantes es un valor no permitido, por favor corrija este valor e ingrese nuevamnete la ruta exacta del archivo *ndice: "
                    else:
                        if(j == math.sqrt(6)):
                            message = "Se*or usuario, la cantidad de archivos es un valor absurdo, por favor corrija este valor e ingrese nuevamente la ruta exacta del archivo *ndice: "
                        else:
                            message = "Se*or usuario, hubo un problema con la ruta del archivo ingresado, por favor intente nuevamente: "
        try:
            archivo = raw_input(message + "\n")
            probar = open(archivo)
            for linea in probar:
                if("porcentaje" in linea or "porcentajes" in linea or "Porcentajes" in linea or "Porcentaje" in linea):
                    probar = linea
                    probar = probar[(probar.index("[") + 1):probar.index("]")]
                    probar = probar.split(",")
                    probar = np.loadtxt(probar)
                    probar = sum(probar)
                    if(probar != 100):
                        probar = math.sqrt(-1)
                    comprobar = open(archivo)
                    comprobar = len(comprobar.readlines())
                    comprobar = 4/comprobar
                if("Estudiantes totales" in linea or "Estudiantes Totales" in linea):
                    filtrar = linea
                    filtrar = int(re.sub("\D", "", filtrar))
                    if(filtrar <= 0):
                        j = math.sqrt(5)
                        return getFileName(j)
                if("Cantidad de Archivos" in linea or "Cantidad de archivos" in linea):
                    filtrar = linea
                    filtrar = int(re.sub("\D", "", filtrar))
                    if(filtrar <= 0):
                        j = math.sqrt(6)
                        return getFileName(j)
            return archivo
        except (IOError):
            j += 1
            return getFileName(j)
        except (OSError):
            j += 1
            return getFileName(j)
        except (ZeroDivisionError):
            j = math.sqrt(2)
            return getFileName(j)
        except(ValueError):
            j = math.sqrt(3)
            return getFileName(j)

    Archivo = getFileName(j)
    print("\n" + str((open(Archivo)).read()))

    keyWord = "Cantidad de Archivos"
    for linea in open(Archivo):
        if(keyWord in linea):
            numArc = linea
            numArc = int(re.sub("\D", "", numArc))
            print("El n*mero de archivos a analizar es: " + str(numArc))

    keyWord = "Estudiantes totales"
    for linea in open(Archivo):
        if(keyWord in linea):
            numEst = linea
            numEst = int(re.sub("\D", "", numEst))
            print("\nEl n*mero de estudiantes es: " + str(numEst))

    for i in range(1, (numArc + 1)):
        vars()["porcentajeEvaluacion%s" % j] = ""

    j = 1
    keyWord = "porcentajes"
    for linea in open(Archivo):
        if(keyWord in linea or "porcentaje" in linea):
            porcentajesEvaluaciones = linea
            porcentajesEvaluaciones = porcentajesEvaluaciones[(porcentajesEvaluaciones.index("[") + 1):(porcentajesEvaluaciones.index("]"))]
            porcentajesEvaluaciones = porcentajesEvaluaciones.split(',')
            for i in range(len(porcentajesEvaluaciones)):
                porcentajesEvaluaciones[i] = float(porcentajesEvaluaciones[i])
            vars()["porcentajeEvaluacion%s" % j] = porcentajesEvaluaciones
            j += 1

    for i in range(1, (numArc + 1)):
        print("\n" + str(vars()["porcentajeEvaluacion%s" % i]))

    j = 0
    for i in range(1, (numArc + 1)):
        vars()["Evaluacion%s" % i] = getFileName(j)

    for i in range(1, (numArc + 1)):
        vars()["Evaluacion%s" % i]
        if("Parcial1" in vars()["Evaluacion%s" % i]):
            Parcial1 = vars()["Evaluacion%s" % i]
            Parcial1 = np.loadtxt((Parcial1))
        if("Parcial2" in vars()["Evaluacion%s" % i]):
            Parcial2 = vars()["Evaluacion%s" % i]
            Parcial2 = np.loadtxt(open(Parcial2))
        if("Practica1" in vars()["Evaluacion%s" % i]):
            Practica1 = vars()["Evaluacion%s" % i]
            Practica1 = np.loadtxt(open(Practica1))
        if("Practica2" in vars()["Evaluacion%s" % i]):
            Practica2 = vars()["Evaluacion%s" % i]
            Practica2 = np.loadtxt(open(Practica2))
        if("PracticaFinal" in vars()["Evaluacion%s" % i]):
            PracticaFinal = vars()["Evaluacion%s" % i]
            PracticaFinal = np.loadtxt(open(PracticaFinal))

    a = Parcial1
    b = Parcial2
    c = Practica1
    d = Practica2
    e = PracticaFinal

    print("\n Notas Parcial 1: ")
    Parcial1 = np.zeros((numEst, 2))
    for i in range(numEst):
        Parcial1[i,0] = i + 1
        Parcial1[i,1] = (sum(a[i,1:]))/20
    print(Parcial1)

    print("\n Notas Parcial 2: ")
    Parcial2 = np.zeros((numEst, 2))
    for i in range(numEst):
        Parcial2[i,0] = i + 1
        Parcial2[i,1] = (sum(b[i,1:]))/20
    print(Parcial2)

    print("\n Notas Pr*ctica 1: ")
    Practica1 = np.zeros((numEst, 2))
    for i in range(numEst):
        Practica1[i,0] = i + 1
        Practica1[i,1] = (sum(c[i,1:]))/20
    print(Practica1)

    print("\n Notas Pr*ctica 2: ")
    Practica2 = np.zeros((numEst, 2))
    for i in range(numEst):
        Practica2[i,0] = i + 1
        Practica2[i,1] = (sum(d[i,1:]))/20
    print(Practica2)

    print("\n Notas Pr*ctica Final: ")
    PracticaFinal = np.zeros((numEst, 2))
    for i in range(numEst):
        PracticaFinal[i,0] = i + 1
        PracticaFinal[i,1] = (sum(e[i,1:]))/20
    print(PracticaFinal)

    print("\n Notas Totales: ")
    NotasEvaluaciones = np.zeros((numEst, numArc + 1))
    for i in range(numEst):
        NotasEvaluaciones[i,0] = i + 1
        NotasEvaluaciones[i,1] = Parcial1[i,1]
        NotasEvaluaciones[i,2] = Parcial2[i,1]
        NotasEvaluaciones[i,3] = Practica1[i,1]
        NotasEvaluaciones[i,4] = Practica2[i,1]
        NotasEvaluaciones[i,5] = PracticaFinal[i,1]
    print(NotasEvaluaciones)

    print("\n Promedio Notas Estudiantes: ")
    PromedioNotas = np.zeros((numEst, 2))
    for i in range(numEst):
        PromedioNotas[i,0] = i + 1
        PromedioNotas[i,1] = Parcial1[i,1]*(15.0/100) + Parcial2[i,1]*(15.0/100) + Practica1[i,1]*(20.0/100) + Practica2[i,1]*(20.0/100) + PracticaFinal[i,1]*(30.0/100)
    print(PromedioNotas)

    print("\n Promedio Notas Evaluaciones: ")
    PromedioNotasEva = np.zeros((numArc, 2))
    for i in range(numArc):
        PromedioNotasEva[i,0] = i + 1
        PromedioNotasEva[0,1] = str((sum(Parcial1[:,1]))/numEst)
        PromedioNotasEva[1,1] = str((sum(Parcial2[:,1]))/numEst)
        PromedioNotasEva[2,1] = str((sum(Practica1[:,1]))/numEst)
        PromedioNotasEva[3,1] = str((sum(Practica2[:,1]))/numEst)
        PromedioNotasEva[4,1] = str((sum(PracticaFinal[:,1]))/numEst)
    print(PromedioNotasEva)

    desvTipica = np.zeros((numEst, 2))
    for i in range(numEst):
        datos = NotasEvaluaciones[i,1:]
        desvTipica[i,0] = i + 1
        desvTipica[i,1] = datos.std(axis = 0)
    print("\n La desviaci*n t*pica para cada estudiante es: " + "\n" + str(desvTipica) )

    desvTipicaTot = np.zeros((numArc, 2))
    for i in range(numArc):
        datos = NotasEvaluaciones[:,i + 1]
        desvTipicaTot[i,0] = i + 1
        desvTipicaTot[i,1] = datos.std(axis = 0)
    print("\n La desviaci*n t*pica para cada evaluaci*n es: " + "\n" + str(desvTipicaTot) )

    for i in range(numEst):
        arregloNotas = NotasEvaluaciones[i,1:]
        vars()["lista%s" % (i + 1)] = arregloNotas
        plt.plot(vars()["lista%s" % (i + 1)])
        plt.xlabel("Evaluaciones")
        plt.ylabel("Notas")
        indice = np.arange(5)
        plt.xticks(indice,("Parcial 1", "Parcial 2", "Pr*ctica 1", "Pr*ctica 2", "Pr*ctica Final"))
    plt.show()

    def gettingResponse(NotasEvaluaciones):
        try:
            options = int(input("\n Se*or usuario, por favor digite el c*digo (n*mero) del estudiante para mostrar su progreso, en caso que no desee ver el progreso de alg*n estudiante presione la tecla 0: \n"))
            if(options < 0 or options > numEst):
                print("\n Se*or usuario, por favor digite un valor v*lido para el n*mero del estudiante, es decir, un n*mero entre 1 y " + str(numEst) + " para recibir una respuesta satisfactoria... ")
                return gettingResponse(NotasEvaluaciones)
            else:
                if(options == 0):
                    return options
                else:
                    arregloNotas = NotasEvaluaciones[options - 1,1:]
                    localVar = arregloNotas
                    Title = plt.figure()
                    Title.suptitle("Estudiante %s" % options)
                    plt.plot(localVar)
                    plt.xlabel("Evaluaciones")
                    plt.ylabel("Notas")
                    indice = np.arange(5)
                    plt.xticks(indice,("Parcial 1", "Parcial 2", "Pr*ctica 1", "Pr*ctica 2", "Pr*ctica Final"))
                    plt.show()
                    return gettingResponse(NotasEvaluaciones)
        except(ValueError):
            print("\n No son v*lidos los n*meros de tipo flotante (float) o cadenas (string) por favor intente con un n*mero del 1 al " + str(numEst) + " para obtener una respuesta safistactoria...")
            return gettingResponse(NotasEvaluaciones)
    gettingResponse(NotasEvaluaciones)
    print("\n A continauci*n se mostrar* el progreso s*lo de aquellos estudiantes que siempre mejoraron sus calificaciones: \n")

    count = 0
    for i in range(numEst):
        if(NotasEvaluaciones[i,1] < NotasEvaluaciones[i,2] < NotasEvaluaciones[i,3] < NotasEvaluaciones[i,4] < NotasEvaluaciones[i,5]):
            arregloNotas = NotasEvaluaciones[i,1:]
            vars()["lista%s" % (i + 1)] = arregloNotas
            plt.plot(vars()["lista%s" % (i + 1)])
            plt.xlabel("Evaluaciones")
            plt.ylabel("Notas")
            indice = np.arange(5)
            plt.xticks(indice,("Parcial 1", "Parcial 2", "Pr*ctica 1", "Pr*ctica 2", "Pr*ctica Final"))
        else:
            count += 1
    if(count == 27):
        print("\n Ning*n estudiante mantuvo un progreso constante durante todas las evaluaciones. \n")
    else:
        plt.show()

    while(True):
        try:
            if(j == 0):
                message = "\n Por favor ingrese 1 para reiniciar el programa o 0 para terminar su ejecuci*n: \n"
            else:
                message = "\n Se*or usuario, por favor digite una entrada v*lida: \n"
            z = int(input(message))
            break
        except:
            j += 1
print("\n ***Gracias por utilizar nuestro software!!!")
