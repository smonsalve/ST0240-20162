# Paradigmas de Programacion
# Procedimientos, tareas... funciones
# Objetos: organizar datos y funcionalidad 
# Clases y Objetos
# una nueva clase crea un nuevo tipo de "algo"
# un objeto es "materializar" una instancia de ese nuevo tipo.
#variables que pertenecen al objeto

class Contacto:
   'clase base para el manejo de contactos'
   ContactCount = 0

   def __init__(self, nombre, correo):
      self.nombre = nombre
      self.correo = correo
      Contacto.ContactCount += 1
   
   def mostrarCuantosContactos(self):
     print "Contactos Totales: %d" % Contacto.ContactCount

   def mostrar(self):
      print "Nombre: ", self.nombre,  ", Correo: ", self.correo

c1 = Contacto("Sergio", "smonsal3@eafit.edu.co")
c2 = Contacto("Andres", "smonsalve@gmail.com")

a = []
a.append(c1)
a.append(c2)

# print c1.mostrarCuantosContactos()
# print c1.mostrar()

for item in a:
	print item.mostrar()
