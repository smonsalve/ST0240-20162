def readCase():
	n = input()
	agenda = []
	for n in range(n):
		agenda.append(str(input()))
	return agenda

def consistente(agenda):
	cons = True
	for item in agenda:
		agenda.remove(item)
		for element in agenda:
			#print item, element[0:len(item)], agenda
			if item == element[0:len(item)]:
				return False
	return cons

t = input()

for i in range(t):
	ordenada = sorted(readCase())
	if consistente(ordenada):
		print "YES"
	else:
		print "NO"
