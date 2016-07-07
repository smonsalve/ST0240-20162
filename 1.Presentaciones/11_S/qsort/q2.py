a = [17, 12, 13, 13, 4, 10, 7, 13, 1, 19]

def quicksort (arreglo) : 
  izquierdo= 0
  derecho = len(arreglo)-1

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
    if izquierdo<d : quicksort(arreglo,izquierdo,d) 
    if i<derecho : quicksort(arreglo,i,derecho) 
  return arreglo 

print quicksort(a)