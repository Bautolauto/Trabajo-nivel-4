#ARREGLAR
for i in range (5):
 vidas = int(input("¿Cuantas vidas queres tener?")) 
 if vidas >= 5:
    dificultad = "facil"
 elif 3 <= vidas < 5:
    dificultad = "medio"
 else : dificultad = "dificil"
 print ("modo",dificultad,"seleccionado")