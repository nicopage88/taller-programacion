import pandas as pd

# Definimos las horas y las materias para cada día de la semana
horas = [
    "08:00-08:45", "08:45-09:30", "09:30-09:45", "09:45-10:30", "10:30-11:15",
    "11:15-11:30", "11:30-12:15", "12:15-13:00", "13:00-13:50", "13:50-14:35",
    "14:35-15:20", "15:20-15:35", "15:35-16:20", "16:20-17:05"
]

# Los días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Datos del horario
# Estos son los nombres de los profesores y materias por cada hora y día
horario = {
    "Lunes": [
        "Matemática", "Lenguaje", "REC", "Felipe/Ing", "Felipe/Ing", "REC", "MJ/Or", "MJ/Or", "REC", "MJ/Leng", "MJ/Leng", "ALM", "", ""
    ],
    "Martes": [
        "", "Matemática", "REC", "C. Fonológica", "C. Fonológica", "REC", "Matemática", "Matemática", "REC", "Matemática", "Matemática", "ALM", "", ""
    ],
    "Miércoles": [
        "Elena/Matem", "Elena/Matem", "REC", "Johanna/Len", "Johanna/Len", "REC", "Inelia/Or", "Inelia/Or", "REC", "Johanna/Or", "Johanna/Or", "ALM", "", ""
    ],
    "Jueves": [
        "Barbara/Mat", "Barbara/Mat", "REC", "Inelia/Leng", "Inelia/Leng", "REC", "Inelia/Leng", "Inelia/Leng", "REC", "Inelia/Leng", "Inelia/Leng", "ALM", "", ""
    ],
    "Viernes": [
        "Camila/Max EF", "Camila/Max EF", "REC", "Beatriz/Mat", "Beatriz/Mat", "REC", "Carla/Leng", "Carla/Leng", "REC", "Felipe/Ing", "Felipe/Ing", "ALM", "", ""
    ]
}

# Convertimos los datos a un DataFrame de pandas
df = pd.DataFrame(horario, index=horas)

# Guardamos el horario en un archivo Excel
archivo_salida = "horario_semana.xlsx"
df.to_excel(archivo_salida, engine='openpyxl', sheet_name='Horario')

# Mensaje indicando que el archivo se ha generado
print(f"Horario guardado en {archivo_salida}")
