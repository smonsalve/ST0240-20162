import matplotlib.pyplot as plt

a = plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.xlabel('esta seria la etiqueta de X')
plt.show()

a.savefig()
