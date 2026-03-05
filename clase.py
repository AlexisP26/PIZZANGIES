class Pizza:
    def __init__ (self, nombre, tamaño,cantidad, precio, oferta):
        self.nombre = nombre
        self.tamaño = tamaño
        self.cantidad = cantidad
        self.precio = precio
        self.disponibilidad = cantidad > 0
        self.oferta = oferta

class Hamburguesa:
    def __init__ (self, nombre, tamaño,cantidad, precio, oferta ):
        self.nombre = nombre
        self.tamaño = tamaño
        self.cantidad = cantidad
        self.precio = precio
        self.disponibilidad = cantidad > 0
        self.oferta = oferta

class Pedido:
    def __init__ (self,producto, cantidad ):
        self.producto = producto
        self.cantidad = cantidad
        self.total = producto.precio * cantidad

