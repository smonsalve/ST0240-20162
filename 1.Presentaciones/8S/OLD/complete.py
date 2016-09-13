import time

archivo = "file.txt"
f = None 

try:
    f = open(archivo)
    while True: 
        line = f.readline() 
        if len(line) == 0:
            break
        print line
        time.sleep(2) 
except FileNotFoundError:
    print("no se puedo encontrar el archivo {}").format(file)
except KeyboardInterrupt:
    print("Cancelado")
finally: 
    if f:
        f.close()
print("Limpiando... : Listo, Archivo cerrado!")