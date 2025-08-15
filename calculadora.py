# mini calculadora

# Pedir operación
operacion = input("Ingrese la operación (suma, resta, multi, divi): ")

# Verificar si la operación existe
if operacion not in ("suma", "resta", "multi", "divi"):
    print("No existe esta operación en mi código.")
else:
    # Pedir números solo si la operación es válida
    x = float(input("Ingrese num1: "))
    y = float(input("Ingrese num2: "))

    # Realizar la operación
    if operacion == "suma":
        resultado = x + y
        print("La suma es:", resultado)
    elif operacion == "resta":
        resultado = x - y
        print("La resta es:", resultado)
    elif operacion == "multi":
        resultado = x * y
        print("La multiplicación es:", resultado)
    elif operacion == "divi":
        if y != 0:
            resultado = x / y
            print("La división es:", resultado)
        else:
            print("Error: No se puede dividir entre cero.")