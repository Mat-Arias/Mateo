def sum(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(input("Ingrese el primer numero: \n"))
num2 = float(input("Ingrese el segundo numero: \n"))

operation = input("Ingrese el operacion:\n") # +, -, *, /
total=""
if operation == "+":
    total = num1 + num2
elif operation == "-":
    total = num1 - num2
elif operation == "*":
    total = num1 * num2
elif operation == "/":
    total = num1 / num2
else:
    print("ERROR OPERATION")
print(total)