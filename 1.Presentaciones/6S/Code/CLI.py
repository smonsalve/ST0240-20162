
def action(c):
	if c == 'q':
		return "gracias por utilizar nuestro software!"


def cli():

	print "oprima la letra segun la accion a realizar: "
	print "para salir oprima q"
	print "printara reiniciar oprima r"
	c = raw_input()
	action(c)

cli()