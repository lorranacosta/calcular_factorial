#ej 8

def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    
    Parámetro:
        n: int - El número entero no negativo para calcular su factorial.
    
    Retorna:
        int: El factorial de n.
    """
    # Si n es 0, el factorial es 1
    if n == 0:
        return 1
    
    # Inicializar el resultado del factorial
    factorial = 1
    
    # Calcular el factorial de n mediante una iteración
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

def main():
    # Solicitar un número entero al usuario
    numero = int(input("Ingrese un número entero: "))
    
    # Verificar si el número es negativo
    if numero < 0:
        print("No se puede calcular el factorial de un número negativo.")
    else:
        # Calcular el factorial del número
        factorial = calcular_factorial(numero)
        # Mostrar el resultado del factorial
        print(f"El factorial de {numero} es: {factorial}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()