class Persona:
    def __init__(self, n, fn):
        self.nombre = n
        self.nacimiento = fn

    def getName(self):
        return self.nombre

    def getNacimiento(self):
        return self.nacimiento

class Estudiante(Persona):

    def __init__(self,n,fn,c):
        Persona.__init__(self,n,fn)
        self.codigo = c1

    def getDatos(self):
        info = ("El estudiante: {} tiene codigo:{}").format(str(self.getName()), str(self.codigo))
        return info


j = Persona("Juan", "14 Abril 2000")
print j.getName()
print j.getNacimiento()

print "___________________"

m = Estudiante("Marcos","19 Noviembre 1997",201510093010)
print m.getDatos()

#print m.getMaterias()