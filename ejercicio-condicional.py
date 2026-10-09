nota=int(float(input("¿Cúal es tu nota? \n\n")))

if nota < 0:
    print("Nota incorrecta")
elif nota >= 0 and nota < 5:
    print("Nota insuficiente")
elif nota >= 5 and nota < 6:
    print("Nota Suficiente")
elif nota >= 6 and nota < 7:
    print("Buena nota")
elif nota >= 7 and nota < 8:
    print("Notable")
elif nota >= 8 and nota <= 10:
    print("Sobresaliente")
if nota > 10:
    print("Nota incorrecta")