a = [17, 12, 13, 13, 4, 10, 7, 13, 1, 19]

def quicksort (arreglo) : 
  ordena_quicksort(arreglo,0,len(arreglo)-1) 
  return arreglo 
 
def ordena_quicksort (arreglo,izquierdo,derecho) : 
  if izquierdo<derecho : 
    pivote=arreglo[(izquierdo+derecho)/2] 
    i,d=izquierdo,derecho 
    while i<=d : 
      while arreglo[i]<pivote : i+=1 
      while arreglo[d]>pivote : d-=1 
      if i<=d : 
        arreglo[i],arreglo[d]=arreglo[d],arreglo[i] 
        i+=1 
        d-=1 
    if izquierdo<d : ordena_quicksort(arreglo,izquierdo,d) 
    if i<derecho : ordena_quicksort(arreglo,i,derecho) 
  return arreglo

print a
print quicksort(a)