

total_space=float(input("¿Cuanto espacio tienes en el disco Duro?\n"))
disk_usage=float(input("dime cuanto espacio esta ocupado\n"))
if total_space > disk_usage:
    print("guardando el archivo")
elif total_space == disk_usage:
    print("No entra el archivo")
else :
    print("ERROR")


