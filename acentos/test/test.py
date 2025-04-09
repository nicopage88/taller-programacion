import pandas as pd

# Función para corregir las Ñ mal codificadas
def corregir_enes(texto):
    # Diccionario de reemplazos comunes para 'Ñ' y 'ñ' mal codificadas
    reemplazos = {
        'NUÃ±EZ': 'NUÑEZ',
        'NUÃ‘EZ': 'NUÑEZ',
        'Ã±': 'ñ',
        'Ã‘': 'Ñ',
        'NUÃ‘EZ': 'NUÑEZ',  # Si hay más casos, añádelos aquí
    }
    
    for clave, valor in reemplazos.items():
        texto = texto.replace(clave, valor)
    return texto

# Cargar el archivo CSV original
df = pd.read_csv('nomina.csv', encoding='utf-8', sep='\t')  # Ajusta el 'sep' si es necesario

# Aplicar la corrección a cada celda del DataFrame
df = df.applymap(lambda x: corregir_enes(str(x)) if isinstance(x, str) else x)

# Guardar el archivo corregido en un nuevo CSV
df.to_csv('nomina_corregida.csv', index=False, sep='\t', encoding='utf-8')

print("Archivo corregido guardado como 'nomina_corregida.csv'")
