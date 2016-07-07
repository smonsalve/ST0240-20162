lintclass Moto:
	'Clase base para el manejo de motos'
	ContadorMotos = 0

	def __init__(self,placa,marca,cili, vel):
		self.placa = placa
		self.marca = marca
		self.cilindraje = cili
		self.velocidad = vel
		Moto.ContadorMotos += 1

	def __str__(self):
		return ("la moto de placa {} con cilindraje {} y marca {} tiene una velocidad de {}").format(self.placa,self.cilindraje,self.marca,self.velocidad)

	def cambiarVelocidad(self,aceleracion):
		temp = self.velocidad 
		if aceleracion > 0:
			temp += aceleracion
		else:
			temp += aceleracion 

		if temp < 0:
			temp = 0
		self.velocidad = temp	

	def cambiarPlaca(self,nuevaPlaca):
		self.placa = nuevaPlaca

# fin clase

ContadorMotos = 1
			

m1 = Moto('TB17A','Honda',200,0)
print m1
print m1.velocidad
m1.cambiarVelocidad(10)
print m1.velocidad
m1.cambiarVelocidad(-15)
print m1.velocidad
print Moto.ContadorMotos
print m1
m2 = Moto('MFS12A',"AKT",110,0)
print m2.placa
print Moto.ContadorMotos

m2.cambiarPlaca('ABC12A')
print m2.placa

print m2

print Moto.ContadorMotos
