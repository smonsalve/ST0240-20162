import random

numero = int(input("ingrese numero magico: "))

def lanzar():
    dado1= random.randint(1, 6)
    dado2= random.randint(1, 6)
    return (dado1,dado2)

lanzamiento = 0
gano = False

while(lanzamiento < 3 or not gano):
    dado1,dado2 = lanzar()
    print (dado1, dado2)
    if(dado1+dado2==numero):
        print("Ganaste!")
        gano = True
    else:
        print("Yucas!")
    lanzamiento += 1
#     
#     if(dado1+dado2==numero):
#             print("Ganaste!")
#     else:
#         dado1= random.randint(1, 6)
#         dado2= random.randint(1, 6)
#         if(dado1+dado2==numero):
#                 print("Ganaste!")

# print (random.randint(2, 12))

