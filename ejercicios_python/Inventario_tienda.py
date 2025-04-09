class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}")

    def actualizar_stock(self, cantidad):
        self.cantidad += cantidad
        print(f"Stock actualizado: {self.cantidad} unidades de {self.nombre}.")

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_inventario(self):
        print(f"Inventario de {self.nombre}:")
        for producto in self.productos:
            producto.mostrar_info()

# Ejemplo de uso
producto1 = Producto("Camiseta", 50, 15.99)
producto2 = Producto("Pantalón", 30, 25.50)

tienda = Tienda("Tienda de Ropa")
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

tienda.mostrar_inventario()
producto1.actualizar_stock(10)
tienda.mostrar_inventario()
