path = 'input/'
h = open (path+"Nombres.txt","r")
for A in h:
        print "\n"
        f = open(path + A.rstrip(),"r")
        line = list(f)

        d1 = map(int, line[1].split())
        b = 0
        if ((d1[0] or d1[1] or d1[2]) == 3) or (d1[0] + d1[1] + d1[2]) == 3:
            b += 1
            if d1[2] != 0:
                d1[2] -= 1
            elif d1[1] != 0:
                d1[1] -= 1
            elif d1[0] != 0:
                d1[0] -= 1
            resultado = (d1[0]*2.5 + d1[1]*2.0 + d1[2]*1.5) + b
        else:
            resultado = d1[0]*2.5 + d1[1]*2.0 + d1[2]*1.5
        d = {A.rstrip() : resultado}
        t = d.keys()
        g = open(path+'Nots.ot','a')
        g.write(t[0] + ' : ' + str(resultado) + '\n')
