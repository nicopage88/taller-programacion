# Importa la función 'obtener_nombre_jugador' desde el archivo 'jugador.py'
from jugador import obtener_nombre_jugador

# Importa las funciones 'modo_de_juego' y 'jugar' desde el archivo 'juego.py'
from juego import modo_de_juego, jugar

# Define la función principal del programa
def main():
    # Solicita el nombre del jugador (debe comenzar con Dr. o Dra.)
    nombre_jugador = obtener_nombre_jugador()

    # Muestra un mensaje de bienvenida personalizado
    print("\n¡Bienvenido al juego de la tabla periódica!")
    print(f"{nombre_jugador}, hoy practicarás tus conocimientos sobre química.")

    # Bucle principal del juego: se repite mientras el jugador quiera seguir jugando
    while True:
        # Muestra el menú y permite elegir el modo de juego
        modo = modo_de_juego()

        # Llama a la función 'jugar' según el modo seleccionado
        resultado = jugar(modo, nombre_jugador)

        # Muestra un mensaje dependiendo si el jugador acertó o no
        if resultado:
            print(f"\n¡Impresionante desempeño, {nombre_jugador}!")
        else:
            print(f"\n¡No te desanimes, {nombre_jugador}! La práctica hace al maestro.")

        # Pregunta si el jugador desea volver a jugar
        jugar_otra = input(f"\n¿Deseas jugar de nuevo, {nombre_jugador}? (yes/no): ").strip().lower()
        if jugar_otra != "yes":
            # Si la respuesta no es "yes", finaliza el juego
            print("\n¡Gracias por jugar! ¡Hasta la próxima!")
            break

# Esta condición se asegura de que el juego solo se ejecute cuando se llame directamente el archivo
if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el juego
