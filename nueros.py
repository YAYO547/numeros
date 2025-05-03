def calcular(n1, operacion, n2):
    if operacion == "+":
        return n1 + n2
    elif operacion == "-":
        return n1 - n2
    elif operacion == "*":
        return n1 * n2
    elif operacion == "/":
        if n2 != 0:
            return n1 / n2
        else:
            print("Error: división por cero.")
            return n1
    else:
        print("Operación no válida.")
        return n1

# Iniciar con un número
n = float(input("Ingrese un número: "))

while True:
    operacion = input("Ingrese una operación (+, -, *, /): ")
    try:
        n2 = float(input("Ingrese otro número: "))
        resultado = calcular(n, operacion, n2)
        print("Resultado:", resultado)
        n = resultado  # Actualizamos n con el resultado
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
