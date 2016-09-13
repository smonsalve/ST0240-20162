path = "input/"
x = "Nombres.txt"
def la(y):
    x = open(path+y,"r+")
    c = []
    for i in (x):
        c.append(i.rstrip())
    x.close()
    return c

def nota(vec):
    c = []
    for i in range(len(vec)):
        b = vec[i].split()
        for y in b:
            d = int(y)
            c.append(d)
    s = 1
    v = 0
    contador = 0
    regula = 0
    for r in range((len(c))-1):
        contador += c[s]
        bonus = 0
        h = c[s]
        if x != 0:
            if regula == 0:
                if contador == 3:
                    bonus = 1
                    h -= 1
                    regula += 1
                elif contador > 3 or h > 3:
                    return "Error: Revise el numero de notas(existe mas de tres notas)"
                    break
        if h == 0:
            s += 1
            v += bonus
            continue
        if s == 4:
            break
        elif c[s] == 3:
            h = c[s] - 1
            bonus = 1
            contador = 0
        if s == 1:
            h *= 2.5
        elif s == 2:
            h *= 2.0
        elif s == 3:
            h *= 1.5
        v += h + bonus
        s += 1
    return(v)

w = open(path+x)
final = open(path+"Notas.ot" ,"w")
for j in w:
    ra = j.partition(".txt")
    k = (la(j.rstrip()))
    q = nota(k)
    g = str(ra[0]+": "+str(q)+"\n")
    final.write(g)
final.close()
w.close()
