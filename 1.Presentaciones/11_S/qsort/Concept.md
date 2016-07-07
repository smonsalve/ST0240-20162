Elegir un elemento de la lista: pivote.
Resituar los demás elementos de la lista a cada lado del pivote,
  a un lado queden todos los menores
  al otro los mayores
  Los elementos iguales al pivote pueden ser colocados tanto a su derecha como a su izquierda, dependiendo de la implementación deseada.

   !!!! En este momento, el pivote ocupa exactamente el lugar que le corresponderá en la lista ordenada.

La lista queda separada en dos sublistas
    una formada por los elementos a la izquierda del pivote,
    y otra por los elementos a su derecha.

Repetir este proceso de forma recursiva para cada sublista mientras éstas contengan más de un elemento.

Una vez terminado este proceso todos los elementos estarán ordenados.
