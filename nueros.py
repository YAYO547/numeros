def calcular(n1,operacion,n2):
    if operacion == "+":
        return n1 + n2
    elif operacion =="-":
        return n1 -n2
    elif operacion == "*":
        return n1 * n2
    elif operacion == "/":
        if n2 != 0:
            return n1 / n2
        else:
            print("Error: division por cero no valida")
            return n1
    else: 
        print("Operacion no valida")
        return n1
    
    # Iniciar con un numero
    n= float(input("Ingrese un numero;"))
    
    while True:
        operacion = input("Ingrese una operacion (+,-,*,/):")
        try:
            n2 = float(input("Ingrese otro numero:"))
            resultado = calcular (n ,operacion,n2)
            print("Resultado:", resultado)
            n= resultado # Actualizamos n con el resultado
        except ValueError:
            print("Entrada no valida. Por favor,ingrese una entrada valida")