total_space= float(input("Dime el espacio total del disco: \n"))
disk_usage= float(input("Dime cuanto espacio esta ocupado: \n"))

def disk_space(total, disk):
    result = ""
    if total > disk:
        result = "Guardando el archivo"
    elif total == disk:
        result = "No entra el archivo"
    else:
        result = "ERROR"
    return result
print(disk_space(total_space, disk_usage))
