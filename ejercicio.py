edad=int(input("Introduce tu Edad:\n"))
estudiante=(input("¿Eres Estudiante?:\n"))
dia=input("Que dia de la semana es?\n")

precio = 8
if dia == "Miercoles" or dia == "Miercoles":
    precio = 4
elif edad < 12:
    precio = 4
    print("Pagas la mitad")
elif edad > 65:
    precio = 5
    print("Precio reducido a 5€")
elif estudiante == "si":
    precio = 5.6
    print("Tienes un descuento del 30%")
else:
    print("ERROR")
print("El precio de la entrada es", precio)