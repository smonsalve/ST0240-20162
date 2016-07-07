uno = [1,2,3]
dos = [2,4,6]
tres = [3,6,9]

a = {"clave1":uno, "clave2":dos, "clave3":tres}


elfile = open("dict.txt")

palabras = set()

for line in elfile:
	words = line.strip('\n').split(' ')
	for item in words:
		palabras.add(item)


index = dict()

for item in palabras:
	lines = open("dict.txt").readlines()
	
	for line in range(0,len(lines)):
		
		if item in lines[line]:
			try:
				index[item]
			except(KeyError):
				index[item] = []
			index[item].append(line+1)

# for line in open("dict.txt"):
# 	print line.strip('\n')

#print palabras

for k,v in index.items():
	print k,v