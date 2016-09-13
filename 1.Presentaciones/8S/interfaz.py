

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b



#print suma(4,5)
#print resta(8,3)
#print suma(1,resta(5,2))


def comandos():
    opcion = ""
    while opcion != '0':
        mensaje = ""
        mensaje += "para sumar oprima 1\n"
        mensaje += "para restar oprima 2\n"
        mensaje += "para salir oprima 0\n"
        
        
        print mensaje
        opcion = raw_input("ingrese la opcion deseada\n")
    
        parametros = "ingrese los dos numeros a operar separados por un espacio\n"

        if int(opcion) == 1:
            a,b = [int(x) for x in raw_input(parametros).split()]
            print suma(a,b)


comandos()
