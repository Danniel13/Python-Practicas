from tkinter import messagebox
nombre = "Francisco"
print("Ingresa tu edad")
edad = input()
if edad.isnumeric():
	edad = int(edad)
	if edad  > 18:
	 print("eres mayor de edad")
	else:
		print("no eres mayor de edad")
else:
	messagebox.showinfo (message="Ingrese un valor numérico", title="Error")