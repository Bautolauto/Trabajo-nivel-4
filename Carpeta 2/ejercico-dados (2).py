import random
bandera = True
veces = int(input("¿cuantas veces queres tirar el dado?"))
if veces == 0:
    print("¿como queres sumar puntos si no tiras crack?")
    bandera = False
if veces <0:
    print("noooo, esto ya es querer hacerme quedar mal")
    bandera = False
Tiradas = 0
puntos = 0
while bandera:
    Tiradas=Tiradas + 1
    puntos=puntos + random.randint(1,6)
    if Tiradas == veces :
        bandera = False
    if bandera : False
    print ("tu puntaje es", puntos,) 
