	import matplotlib.pyplot as plt
	import numpy as np
	import csv

a =  np.loadtxt(open("Archivo.csv","rU"),delimiter=",",usecols=(0,1))

result = a[a[:, 1].argsort()]
# print result

plt.bar(result[:,0],result[:,1])

plt.xlabel('Estudiante')
plt.ylabel('Nota')
plt.title('Primer Parcial')
#plt.grid(True)
#plt.savefig("test.png")
plt.show()