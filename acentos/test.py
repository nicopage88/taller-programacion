import pandas as pd
from unidecode import unidecode

# Función para quitar acentos y reemplazar 'ñ' por 'n'
def quitar_acentos_y_enes(texto):
    if isinstance(texto, str):
        # Reemplazar ñ por n y quitar acentos
        texto = texto.replace('ñ', 'n')
        texto = unidecode(texto)
    return texto

# Función para procesar el archivo CSV
def procesar_archivo_csv(archivo_entrada, archivo_salida):
    # Leer el archivo CSV con delimitador de tabulación y codificación ISO-8859-1
    df = pd.read_csv(archivo_entrada, encoding='ISO-8859-1', sep='\t')
    
    # Limpiar los nombres de las columnas eliminando espacios extras
    df.columns = df.columns.str.strip()

    # Verificar las primeras filas y las columnas del archivo
    print("Columnas del archivo CSV:", df.columns)  # Imprimir las columnas
    print(df.head())  # Mostrar las primeras filas para verificar los datos

    # Asegurarse de que las columnas relevantes estén presentes
    columnas_relevantes = ['nombre', 'apellido', 'curso']
    
    # Verificar si las columnas están en el archivo CSV
    if all(col in df.columns for col in columnas_relevantes):
        # Aplicar la función quitar_acentos_y_enes a las columnas relevantes
        df[columnas_relevantes] = df[columnas_relevantes].applymap(quitar_acentos_y_enes)
        
        # Guardar el DataFrame procesado en un nuevo archivo CSV
        df.to_csv(archivo_salida, index=False, encoding='ISO-8859-1')
    else:
        print(f"Error: Las siguientes columnas no están presentes en el archivo: {', '.join([col for col in columnas_relevantes if col not in df.columns])}")

# Rutas de los archivos de entrada y salida
archivo_entrada = 'datos.csv'
archivo_salida = 'datos_corregidos.csv'

# Procesar el archivo CSV
procesar_archivo_csv(archivo_entrada, archivo_salida)
