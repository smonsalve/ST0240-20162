a = 'Hello'
b = 'java'
c = 'Hi'

def left2(str):
	h = str(-1)
	e = str(-2)
	l = str(0)
	o = str(1)

	n_str = str[:]
	n_str[0] = h
	n_str[1] = e
	n_str[-1] = o
	n_str[-2] = l

	return n_str

print(left2(a))