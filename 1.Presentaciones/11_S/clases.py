import random

class Carta():
    
    def __init__(self, p , v):
        self.pinta = p
        self.valor = v

    def __str__(self):
        return ("{}:{}").format(self.valor,self.pinta)
        # tipo = ""
        # if (self.valor == 11):
        #     tipo +=  "J"
        # if(self.pinta == "Corazones"):
        #    tipo += "<3"
        # return tipo

pintas = ["Corazon","Trebol", "Diamante", "Pica"]

cartas = []

for i in range(11):
    p = pintas[random.randint(0,3)]
    v = random.randint(1,13)
    cartas.append(Carta(p,v))


# for item in cartas:
#     print item


# c1 = Carta("Corazones", 3)
# c2 = Carta("Corazones", 11)

# print c1.pinta
# print c1.valor

# print c2

print cartas[6].pinta
