from clase import Pizza
from clase import Pedido
from clase import Hamburguesa

class Pizzeria:
    def __init__(self):
        self.menu = [
            [
                Pizza("hawaiana1", "pequeña",0, 10000, True),
                Pizza("hawaiana2", "mediana",50, 12000, False),
                Pizza("hawaiana3", "grande",60, 15000, False), 
                Hamburguesa("clasica", "pequeña",10, 8000, True),
                Hamburguesa("especial", "mediana",20, 10000, False),
                Hamburguesa("vip", "grande",15, 15000, False)

            ]
        ]


        self.pedidos = [[Pedido(Pizza("hawaiana1", "pequeña",0, 10000, True), 2),
                        Pedido(Pizza("hawaiana2", "mediana",50, 12000, False), 1),
                        Pedido(Pizza("hawaiana3", "grande",60, 15000, False), 3),
                        Pedido(Hamburguesa("clasica", "pequeña",10, 8000, True), 4),],

                        [Pedido(Hamburguesa("especial", "mediana",20, 10000, False), 2),
                        Pedido(Hamburguesa("vip", "grande",15, 15000, False), 1), 
                        Pedido(Pizza("hawaiana3", "grande",60, 15000, False), 3)
                        ]]

    def mostrar_menu(self):
        print("---- MENÚ DE PIZZAS ----")
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                pizza = self.menu[i][j]
                if pizza is not None:
                   print( pizza.nombre,pizza.tamaño,
                         pizza.cantidad,pizza.precio)
                   
    def buscar_pizza_por_nombre(self, nombre_buscado):
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                pizza = self.menu[i][j]
                if pizza.nombre.lower() == nombre_buscado.lower():
                    return (i, j)
        return None
    
    def calcular_inventario_total(self):
        total = 0
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                producto = self.menu[i][j]
                if producto is not None:
                    total = total + producto.cantidad
                    return total 
   
    def buscar_pizza_mas_costosa(self):
        pizza_mas_costosa = None
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                producto = self.menu[i][j]
                if producto is not None:
                    if pizza_mas_costosa is None or producto.precio > pizza_mas_costosa.precio:
                        pizza_mas_costosa = producto
        return pizza_mas_costosa
   
    def ordenar_ascendente(self):
        self.menu[0].sort(key=lambda x : x.precio) 

    def Disponibilidad(self):
        pizzas_disponibles=[]
        for i in range(len(self.menu)):
            filas_que_iran_en_pizzas_disponibles=[]
            for j in range(len(self.menu[i])):
                pizza = self.menu[i][j]
                if pizza.disponibilidad == True:
                    filas_que_iran_en_pizzas_disponibles.append(pizza)
            if filas_que_iran_en_pizzas_disponibles:
                pizzas_disponibles.append(filas_que_iran_en_pizzas_disponibles)
        return pizzas_disponibles

    def agrupar_por_precio(self):
        economicas=[]
        medias=[]
        premium=[]
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                pizza = self.menu[i][j]
                if pizza.precio < 10000:
                    economicas.append(pizza)
                elif pizza.precio >= 10000 and pizza.precio <= 30000:
                    medias.append(pizza)
                elif pizza.precio > 30000:
                    premium.append(pizza)
                else:
                    print("valor fuera de rango")
        return economicas, medias,premium
    
    def organizar_por_tamaño(self):
        pequeñas = []
        medianas = []
        grandes = []

        for producto in self.productos:
            if producto.tamaño == "pequeña":
                pequeñas.append(producto)

            elif producto.tamaño == "mediana":
                medianas.append(producto)

            elif producto.tamaño == "grande":
                grandes.append(producto)

        self.menu = [
            pequeñas,
            medianas,
            grandes
        ]

    def agregar_producto(self):
        nombre = input("ingrese el nombre que le va dar al producto")
        tamaño = input("ingrese el tamaño que le va dar al producto")
        precio = float(input("ingrese el precio que le va dar al producto"))
        cantidad = int(input("ingrese la cantidad que le va dar al producto"))
        producto = input("escriba que tipo de producto quiere crear: pizza o hamburguesa")
        if producto.lower() == "pizza":
            producto = Pizza(nombre, tamaño, precio, cantidad)

        elif producto.lower == "hamburguesa":
            producto = Hamburguesa(nombre, tamaño, precio, cantidad)
        else:
            print("producto no encontrado")
        self.menu[0].append(producto)
        print("producto agregado con exito")

    def contar_productos_en_oferta(self):
        contador = 0
        for i in range(len(self.menu)):
            for j in range(len(self.menu[i])):
                todos_los_productos = self.menu[i][j]
                if todos_los_productos.oferta == True:
                    contador += 1
        return contador

    def vendedor_con_mas_ventas(self, pedidos):
        total_del_mayor_vendedor = 0
        mejor_vendedor = None
        for i in range(len(pedidos)):
            suma=0
            for j in range(len(pedidos[i])):
                pedido = pedidos[i][j]
                suma+= pedido.total
            if suma > total_del_mayor_vendedor:
                total_del_mayor_vendedor=suma
                mejor_vendedor = i
        return mejor_vendedor, total_del_mayor_vendedor

