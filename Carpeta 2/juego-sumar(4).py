import random

#se que debe haber una mejor manera de hacerlo, pero poner 2 funciones fue lo que me dio un mejor resultado
def dado1():
    cantidad = int(input("Jugador 1 ¿Cuántos dados querés tirar? "))
    suma = 0
    for i in range (cantidad):
     dado = random.randint(1, 6)
     suma = suma + dado
     print (f"Dado {i+1}: {suma}")
    
    return suma

def dado2():
    cantidad = int(input("Jugador 2 ¿Cuántos dados querés tirar? "))
    suma = 0
    for i in range (cantidad):
     dado = random.randint(1, 6)
     suma = suma + dado
     print (f"Dado {i+1}: {suma}")
    
    return suma
    

#contadores
jugador1 = dado1()
jugador2 = dado2()
print ("jugador1 saco", jugador1, "puntos")
print ("jugador2 saco", jugador2, "puntos")

