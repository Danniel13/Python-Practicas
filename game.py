import random	
x = random.randint(0,3)
colores = ["rojo","verde","amarillo","azul"]
puntos = 0
print("Aadivina el color que estoy pensando [rojo,verde,amarillo,azul]")
jugador = input()
if jugador == colores[x]:
	print("Ganaste")
	puntos = puntos + 1
else:
	print("Lo sentimos, el numero era el", colores[x])