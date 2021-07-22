print("Reto #1 Animo")
x=3
y=5
numeros=[]
for i in range (2000):
	if i%x==0:
		numeros.append(i)
	elif i%y==0:
		numeros.append(i)
print(numeros)
suma=0
for i in numeros:
	suma+=i
print(suma)