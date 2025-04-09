class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def es_aprobado(self):
        # Método que verifica si el estudiante aprobó
        if self.calificacion >= 4:
            return True
        else:
            return False

class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_resultados(self):
        for estudiante in self.estudiantes:
            estado = "Aprobado" if estudiante.es_aprobado() else "Reprobado"
            print(f"{estudiante.nombre}: {estado} ({estudiante.calificacion})")

# Ejemplo de uso
estudiante1 = Estudiante("Luis", 7)
estudiante2 = Estudiante("María", 3)
estudiante3 = Estudiante("José", 4)

escuela = Escuela("Escuela Secundaria")

escuela.agregar_estudiante(estudiante1)
escuela.agregar_estudiante(estudiante2)
escuela.agregar_estudiante(estudiante3)

escuela.mostrar_resultados()
