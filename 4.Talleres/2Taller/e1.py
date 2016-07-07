archivo = "file1.txt"
file = open(archivo)

n = int(file.readline())
a = []

for i in range(n):
	a.append(file.readline().rstrip('\n'))

print a