def factorial(n):
    resultado = 1
    if n>2:
        resultado *= factorial(n-1)
    else:
        return resultado

n = int(input())
for i in range(n):
    item = int(input())
    #print item
    print factorial(item)
