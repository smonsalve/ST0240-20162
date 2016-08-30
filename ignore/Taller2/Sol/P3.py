t = int(raw_input())

def zanb(lista):
    impo = 0
    for i in range(len(lista)):
        if lista[i] == 0: break
        if lista[i+1] > lista[i]*2:
            impo += lista[i+1]-lista[i]*2
    return impo

for i in range(t):
    a = [int(x) for x in raw_input().split()]
    print zanb(a)
