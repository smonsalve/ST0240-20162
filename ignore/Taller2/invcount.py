t = int(raw_input())

def lasuma(lista):
    newlist = []
    for item in lista:
        newlist.append(item+1)
    return newlist

for i in range(t):
    nada = raw_input()
    n = int(raw_input())
    lista = []
    for j in range(n):
        elemento = int(raw_input())
        lista.append(elemento)
    print lista
    print lasuma(lista)
