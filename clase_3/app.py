class Persona:
    def __init__(self, nombre, edad, color_pelo, color_ojos):
        self.nombre = nombre
        self.edad = edad
        self.color_pelo = color_pelo
        self.color_ojos = color_ojos

    def hablar(self):
        print(f"{self.nombre} está hablando.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def reir(self):
        print(f"{self.nombre} está riendo a carcajadas.")

    def mostrar_color_pelo(self):
        print(f"{self.nombre} tiene el pelo de color {self.color_pelo}.")

    def mostrar_color_ojos(self):
        print(f"{self.nombre} tiene los ojos de color {self.color_ojos}.")

    def correr(self):
        print(f"{self.nombre} está corriendo rápidamente.")

    def saltar(self):
        print(f"{self.nombre} está saltando de alegría.")

    def jugar(self, juego):
        print(f"{self.nombre} está jugando a {juego}.")

    def tocar_musica(self, instrumento):
        print(f"{self.nombre} está tocando el/la {instrumento}.")

# Crear una persona llamada Ana con más atributos
ana = Persona("Ana", 25, "castaño", "verdes")
pedro = Persona("Pedro", 22, "Negro", "Azules")

# Probar todos los métodos
ana.hablar()
ana.dormir()
ana.reir()
ana.mostrar_color_pelo()
ana.mostrar_color_ojos()
ana.correr()
ana.saltar()
ana.jugar("ajedrez")
ana.tocar_musica("guitarra")

pedro.hablar()
pedro.dormir()
pedro.reir()
pedro.mostrar_color_pelo()
pedro.mostrar_color_ojos()
pedro.correr()
pedro.saltar()
pedro.jugar("pelota")
pedro.tocar_musica("batería")