import random
from elementos import elementos

def modo_de_juego():
    print("\nElige el modo de juego:")
    print("1. Adivinar el número atómico")
    print("2. Adivinar el nombre del elemento")
    print("3. Adivinar el símbolo del elemento")

    while True:
        try:
            opcion = int(input("Selecciona un modo (1-3): "))
            if 1 <= opcion <= 3:
                return opcion
            print("Por favor, ingresa un número entre 1 y 3.")
        except ValueError:
            print("Entrada inválida. Introduce un número")

def jugar(modo, nombre_jugador):
    num_atomico, (nombres, simbolo) = random.choice(list(elementos.items()))
    nombre_elemento = nombres[0]
    intentos = 0
    max_intentos = 5

    print(f"\n¡Vamos a jugar, {nombre_jugador}! Tienes {max_intentos} intentos.")

    if modo == 1:
        print(f"El elemento es: {nombre_elemento} ({simbolo})")
        respuesta_correcta = str(num_atomico)
        pregunta = "¿Cuál es su número atómico?"
    elif modo == 2:
        print(f"Número atómico: {num_atomico}, Símbolo: {simbolo}")
        respuesta_correcta = nombre_elemento.lower()
        pregunta = "¿Cuál es su nombre del elemento?"
    else:
        print(f"Número atómico: {num_atomico}, Nombre: {nombre_elemento}")
        respuesta_correcta = simbolo.lower()
        pregunta = "¿Cuál es su símbolo químico?"

    while intentos < max_intentos:
        intentos += 1
        guess = input(f"\n{pregunta} (Intento {intentos}/{max_intentos}): ").strip().lower()
        if guess == respuesta_correcta:
            print(f"¡Correcto, {nombre_jugador}! El número atómico de {nombre_elemento} es {num_atomico}.")
            return True
        else:
            print(f"Incorrecto. Te quedan {max_intentos - intentos} intentos.")
            if intentos == max_intentos:
                print(f"\nLo siento, {nombre_jugador}. Has agotado tus intentos. Era el {num_atomico}.")

    return False