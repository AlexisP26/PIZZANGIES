class Pizza:
    def __init__ (self, nombre, tamaño,cantidad, precio ):
        self.nombre = nombre
        self.tamaño = tamaño
        self.cantidad = cantidad
        self.precio = precio
        self.disponibilidad = cantidad > 0

class Pedido:
    def __init__ (self,pizza, cantidad ):
        self.pizza = pizza
        self.cantidad = cantidad
        self.total = pizza.precio*cantidad


