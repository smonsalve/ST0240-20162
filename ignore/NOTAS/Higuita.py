path = 'input/'

def Casos():
    h = open (path +"Nombres.txt","r")
    for linea in h:
        f = open(path+linea.rstrip(),"r")
        line = list(f)
        print line [0], line[1]
        d1 = map(int, line[1].split())
        b = 0
        if ((d1[0] or d1[1] or d1[2]) == 3) or (d1[0] + d1[1] + d1[2]) == 3:
            b += 1
            if d1[2] != 0:
                d1[2] -= 1
            elif d1[1] != 0:
                d1[1] -= 1
            elif d1[0] !=0:
                d1[0] -= 1
            Nota=(d1[0]*2.5 + d1[1]*2.0 + d1[2]*1.5) + b
        else:
            Nota=d1[0]*2.5 + d1[1]* 2.0 + d1[2]*1.5
        print Nota
        Notas={}
        Notas[linea.rstrip()] = str(Nota)
        k=open(path + 'Notas.ot','a')
        z=Notas.keys()
        k.write(z[0]+':'+ str(Nota)+ '\n' )
    return Nota
Casos ()

