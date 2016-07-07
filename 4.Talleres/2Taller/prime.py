import random

cantidad = 20
valorMin = 0
valorMax = 20

a = []

for i in range(cantidad):
	a.append(random.randint(valorMin,valorMax))

def isPrime(val):
	prime = True
	for i in range(2,val):
		if(item%i==0):
			prime = False
	return prime

print a

for item in a:
	if isPrime(item):
		f = "es"
	else:
		f = "no es"
	print ("{} {} primo").format(item, f)
