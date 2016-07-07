num = 10

den = 0


for i in range(5):

	try:
		print num/den
	except(ZeroDivisionError):
		print "division por cero"
	
	den+=1