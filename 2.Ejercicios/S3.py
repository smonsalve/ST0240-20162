def pivotes(a):
    cont = 0
    while(a!=1):
        cont = cont + 1
        if(a%2!=0):
            a=3*a+1
        else:
            a=a/2
    return cont

# print(pivotes(1081))

def miFactorial(a):
    resultado = a
    while(a>1):
        resultado = resultado*(a-1)
        a = a-1
    return resultado

print(miFactorial(4))
