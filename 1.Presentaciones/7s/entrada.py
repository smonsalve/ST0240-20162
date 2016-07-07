import sys
import time

archivo = "poem.txt"

f = None 
try:
    f = open(archivo)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("presione ctrl+c ahora")
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print("No se pudo encontrar el archivo")
except KeyboardInterrupt:
    print("!! cancelo la lectura del archivo")
finally:
    if f:
        f.close()
    print("(Limpiar: Archivo cerrado)")