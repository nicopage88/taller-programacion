# Clase base: Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descripcion(self):
        return f"'{self.titulo}' escrito por {self.autor}"

# Clase derivada: LibroDigital
class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)  # Llama al constructor de la clase base
        self.formato = formato

    def leer(self):
        return f"Abriendo el libro digital '{self.titulo}' en formato {self.formato}"

# Crear instancias de ambas clases
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
libro2 = LibroDigital("Python para Todos", "Raúl González", "PDF")

# Mostrar el comportamiento de los objetos
print(libro1.descripcion())
print(libro2.descripcion())  # Hereda método de la clase base
print(libro2.leer())         # Método exclusivo de la clase hija

"""
✅ Conceptos enseñados:
- Clase: 'Libro' define un modelo de objeto.
- Constructor (__init__): Método especial que inicializa el objeto.
- Herencia: 'LibroDigital' hereda de 'Libro'.
- Método: Comportamiento de los objetos.
- Encapsulamiento: Cada objeto tiene sus propias propiedades.
"""
