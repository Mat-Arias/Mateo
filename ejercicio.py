edad=int(input("Introduce su edad:\n"))
estudiante=input("Eres estudiante:\n")
dia=input("¿Que dia es?:\n")

precio=8
if dia == "Miercoles" or dia == "Miercoles":
    precio=4
elif edad < 12:
    precio=4
elif edad > 65:
    precio=5
elif estudiante == "Si":
    precio=5.6
print("El precio de tu entrada es",precio)