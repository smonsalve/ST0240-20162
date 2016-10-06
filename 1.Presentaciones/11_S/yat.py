import random

class Dado():

    valor = None

    def __init__(self, lad, v=None):
        self.lados = lad        

    def roll(self):
        self.valor = random.randint(1,self.lados)
    
def cli(opcion = ""):
    opcion = raw_input()
    
def p_dados(dados):
    vals  = []
    for item in dados:
        vals.append(item.valor)
    print vals

def lanzar(dados):
    for i in dados:
        i.roll()
    return dados


losdados = []

for i in range(5):
    losdados.append(Dado(6))

p_dados(losdados)
p_dados(lanzar(losdados))

#print losdados[0]

b = lanzar(losdados)
p_dados(b)


p_dados(lanzar(losdados))
#print losdados[0]
#print losdados[1]


otrosdados = []
for i in range(3):
    otrosdados.append(Dado(12))

p_dados(lanzar(otrosdados))
    
    
    
