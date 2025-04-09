class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def es_adulto(self):
        # Método que verifica si la persona es mayor de edad
        if self.edad >= 18:
            return True
        else:
            return False

class Botilleria:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def vender(self, persona):
        if persona.es_adulto():
            return f"{persona.nombre}, puedes comprar alcohol en {self.nombre}."
        else:
            return f"{persona.nombre}, no puedes comprar alcohol. Debes tener 18 años o más."

# Ejemplo de uso
persona1 = Persona("Carlos", 20)
persona2 = Persona("Ana", 16)
persona3 = Persona("Pedro", 18)
persona4 = Persona("Juana", 17)
persona5 = Persona("Anamaría", 21)
persona6 = Persona("Anita", 99)

botilleria = Botilleria("La Botillería de la Esquina")

print(botilleria.vender(persona1))  # Carlos puede comprar
print(botilleria.vender(persona2))  # Ana no puede comprar
print(botilleria.vender(persona3))  
print(botilleria.vender(persona4))  
print(botilleria.vender(persona5))  
print(botilleria.vender(persona6))  
