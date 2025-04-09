def fibonacci(n):
    # Lista que almacenará los números de la sucesión
    fib_sequence = []

    # Los primeros dos términos son siempre 0 y 1
    a, b = 0, 1
    
    # Generar la sucesión hasta el número n
    for _ in range(n):
        fib_sequence.append(a)  # Añadir el número actual a la lista
        a, b = b, a + b  # Actualizar a y b para el siguiente número
    
    return fib_sequence

# Pedir al usuario cuántos términos de la sucesión quiere generar
n = int(input("¿Cuántos términos de la sucesión de Fibonacci deseas generar? "))

# Llamar a la función y mostrar el resultado
resultado = fibonacci(n)
print(f"Los primeros {n} términos de la sucesión de Fibonacci son: {resultado}")
