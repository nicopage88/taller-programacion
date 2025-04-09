import random

#lista de tabla de periodica
elementos = {
    1: (["Hidrógeno"],"H"),
    2: (["Helio"], "He"),
    3: (["Litio"], "Li"),
    4: (["Berilio"], "Be"),
    5: (["Boro"], "B"),
    6: (["Carbono"], "C"),
    7: (["Nitrógeno"], "N"),
    8: (["Oxígeno"], "O"),
    9: (["Flúor"], "F"),
    10: (["Neón"], "Ne"),
    11: (["Sodio"], "Na"),
    12: (["Magnesio"], "Mg"),
    13: (["Aluminio"], "Al"),
    14: (["Silicio"], "Si"),
    15: (["Fósforo"], "P"),
    16: (["Azufre","Sulfuro"], "S"),
    17: (["Cloro"], "Cl"),
    18: (["Argón"], "Ar"),
    19: (["Potasio"], "K"),
    20: (["Calcio"], "Ca"),
    21: (["Escandio"], "Sc"),
    22: (["Titanio"], "Ti"),
    23: (["Vanadio"], "V"),
    24: (["Cromo"], "Cr"),
    25: (["Manganeso"], "Mn"),
    26: (["Hierro"], "Fe"),
    27: (["Cobalto"], "Co"),
    28: (["Níquel"], "Ni"),
    29: (["Cobre"], "Cu"),
    30: (["Zinc"], "Zn"),
    31: (["Galio"], "Ga"),
    32: (["Germanio"], "Ge"),
    33: (["Arsénico"], "As"),
    34: (["Selenio"], "Se"),
    35: (["Bromo"], "Br"),
    36: (["Kriptón"], "Kr"),
    37: (["Rubidio"], "Rb"),
    38: (["Estroncio"], "Sr"),
    39: (["Itrio"], "Y"),
    40: (["Zirconio"], "Zr"),
    41: (["Niobio"], "Nb"),
    42: (["Molibdeno"], "Mo"),
    43: (["Tecnecio"], "Tc"),
    44: (["Rutenio"], "Ru"),
    45: (["Rodio"], "Rh"),
    46: (["Paladio"], "Pd"),
    47: (["Plata"], "Ag"),
    48: (["Cadmio"], "Cd"),
    49: (["Indio"], "In"),
    50: (["Estaño"], "Sn"),
    51: (["Antimonio"], "Sb"),
    52: (["Telurio"], "Te"),
    53: (["Yodo"], "I"),
    54: (["Xenón"], "Xe"),
    55: (["Cesio"], "Cs"),
    56: (["Bario"], "Ba"),
    57: (["Lantano"], "La"),
    58: (["Cerio"], "Ce"),
    59: (["Praseodimio"], "Pr"),
    60: (["Neodimio"], "Nd"),
    61: (["Prometio"], "Pm"),
    62: (["Samario"], "Sm"),
    63: (["Europio"], "Eu"),
    64: (["Gadolinio"], "Gd"),
    65: (["Terbio"], "Tb"),
    66: (["Disprosio"], "Dy"),
    67: (["Holmio"], "Ho"),
    68: (["Erbio"], "Er"),
    69: (["Tulio"], "Tm"),
    70: (["Iterbio"], "Yb"),
    71: (["Lutecio"], "Lu"),
    72: (["Hafnio"], "Hf"),
    73: (["Tántalo"], "Ta"),
    74: (["Wolframio","Tungsteno"], "W"),
    75: (["Renio"], "Re"),
    76: (["Osmio"], "Os"),
    77: (["Iridio"], "Ir"),
    78: (["Platino"], "Pt"),
    79: (["Oro"], "Au"),
    80: (["Mercurio"], "Hg"),
    81: (["Talio"], "Tl"),
    82: (["Plomo"], "Pb"),
    83: (["Bismuto"], "Bi"),
    84: (["Polonio"], "Po"),
    85: (["Astato"], "At"),
    86: (["Radón"], "Rn"),
    87: (["Francio"], "Fr"),
    88: (["Radio"], "Ra"),
    89: (["Actinio"], "Ac"),
    90: (["Torio"], "Th"),
    91: (["Protactinio"], "Pa"),
    92: (["Uranio"], "U"),
    93: (["Neptunio"], "Np"),
    94: (["Plutonio"], "Pu"),
    95: (["Americio"], "Am"),
    96: (["Curio"], "Cm"),
    97: (["Berkelio"], "Bk"),
    98: (["Californio"], "Cf"),
    99: (["Einstenio"], "Es"),
    100: (["Fermio"], "Fm"),
    101: (["Mendelevio"], "Md"),
    102: (["Nobelio"], "No"),
    103: (["Laurencio"], "Lr"),
    104: (["Rutherfordio"], "Rf"),
    105: (["Dubnio"], "Db"),
    106: (["Seaborgio"], "Sg"),
    107: (["Bohrio"], "Bh"),
    108: (["Hassio"], "Hs"),
    109: (["Meitnerio"], "Mt"),
    110: (["Darmstadtio"], "Ds"),
    111: (["Roentgenio"], "Rg"),
    112: (["Copernicio"], "Cn"),
    113: (["Nihonio"], "Nh"),
    114: (["Flerovio"], "Fl"),
    115: (["Moscovio"], "Mc"),
    116: (["Livermorio"], "Lv"),
    117: (["Tenesino"], "Ts"),
    118: (["Oganesón"], "Og"),
}
# Definición de la función para jugar
def obtener_nombre_jugador():
    nombre = input("¡Bienvenido al Laboratorio de Química Interactiva!\n¿Cuál es tu nombre, científico/a? ").strip()
    if not nombre.startswith(("Dr.", "Dra.")):
        print("¡Espera un momento!")
        print("¡No puedes jugar sin ser un doctor!")
        print("¡Recuerda que debes ser un doctor para jugar!")
        print("¡No olvides ingresar tu nombre!")
        return obtener_nombre_jugador()
    print(f"¡Hola, {nombre}! Vamos a jugar.")
    return nombre

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
    num_atomico, (nombre_elemento, simbolo) = random.choice(list(elementos.items()))
    intentos = 0
    max_intentos = 5

    print(f"\n¡Vamos a jugar, {nombre_jugador}!, tienes {max_intentos} intentos!")

    if modo == 1: #numero atomico
        print(f"El elemento es: {nombre_elemento} ({simbolo})")
        respuesta_correcta = str(num_atomico)
        pregunta = "¿Cuál es su número atómico?"
    elif modo == 2: #nombre atómico
        print(f"Número atómico: {num_atomico}, Nombre: {simbolo}")
        respuesta_correcta = nombre_elemento[0].lower()
        pregunta = "¿Cuál es su nombre del elemento?"
    else: #simbolo atomico
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
                print(f"\nLo siento, {nombre_jugador}. Has agotado tus intentos. El número atómico de {nombre_elemento} es {num_atomico}.")

    return False
#inicio del juego
nombre_jugador = obtener_nombre_jugador()
print("\n¡Bienvenido al juego de la tabla periódica!")
print(f"{nombre_jugador}, hoy practicarás tus conocimientos sobre la tabla periódica.")

while True:
    modo = modo_de_juego()
    resultado = jugar(modo, nombre_jugador)

    #mensaje según el resultado
    if resultado:
        print(f"\n¡Impresionante desempeño, {nombre_jugador}!")
    else:
        print(f"\n¡No te desanimes, {nombre_jugador}! La práctica hace al maestro.")

    if input(f"\n¿Deseas jugar de nuevo en el laboratorio, {nombre_jugador}? (yes/no): ").lower() != "yes":
        print(f"\n¡Gracias por jugar! ¡Hasta la próxima!")
        break

