def obtener_nombre_jugador():
    nombre = input("¡Bienvenido al Laboratorio de Química Interactiva!\n¿Cuál es tu nombre, científico/a? ").strip()
    if not nombre.startswith(("Dr.", "Dra.")):
        print("¡Debes ser un doctor o doctora para jugar!")
        return obtener_nombre_jugador()
    print(f"¡Hola, {nombre}! Vamos a jugar.")
    return nombre