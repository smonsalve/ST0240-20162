t = int(raw_input())

def invCont (lista):
    cont = 0
    for i in range(len(lista)-1):
        j = i+1
        if lista[i]>lista[j]: cont+=1 
    return cont

for i in range(t):
    nada = raw_input()
    n = int(raw_input())
    lista = []
    for j in range(n):
        elemento = int(raw_input())
        lista.append(elemento)

    print invCont(lista)
    #print lista