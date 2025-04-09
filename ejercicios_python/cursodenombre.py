import re

def separar_nombre_y_curso(cadena):
    # Usamos una expresión regular más flexible para capturar cursos con números y letras
    # También captura cursos como "IMA", "IIIMA", etc.
    pattern = r"([A-ZÑÁÉÍÓÚ\s]+)\s+(\d+\s+[A-Za-z]+[A-Za-z0-9]*\s+[A-Za-z]+|[A-Za-z]+)\s*"
    
    # Encontrar todas las coincidencias
    coincidencias = re.findall(pattern, cadena)

    # Crear una lista para almacenar los resultados en el formato deseado
    resultados = []

    # Procesamos cada coincidencia
    for coincidencia in coincidencias:
        nombre_completo = coincidencia[0].strip()
        curso = coincidencia[1].strip()  # Asegurarnos de que no haya saltos de línea extras
        resultados.append(f"{nombre_completo}-{curso}")  # Usamos el guion sin espacio

    return resultados

def guardar_resultados_en_txt(resultados, nombre_archivo):
    # Abrir el archivo en modo escritura
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for linea in resultados:
            archivo.write(linea + "\n")

# Texto de ejemplo con cursos tipo IMA, IIMB, IIIMA, etc.
texto = """
AGUSTIN ARGENS RUBEN SUMONTE NUNEZ  1 basico B
FLORENCIA PASCAL MENDEZ GALLEGOS  2 basico B
ANTHONELLA POLETTE ALVAREZ COLIL  2 basico A
PEDRO GOMEZ LOPEZ  IMA
JUAN PEREZ  IIMB
MARIA FERNANDEZ  IIIMA
LUIS MARTINEZ  IVMA
CARLOS GUTIERREZ  IVMB
"""

# Llamar a la función para separar nombres y cursos
resultado = separar_nombre_y_curso(texto)

# Guardar los resultados en un archivo de texto
nombre_archivo = "resultados_cursos.txt"
guardar_resultados_en_txt(resultado, nombre_archivo)

print(f"Los resultados se han guardado en {nombre_archivo}")
