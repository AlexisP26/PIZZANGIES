#mostrar menu
# #crear pedido
#mostrar pedido
from clase import Pizza


class Pizzeria:
    def __init__(self):
        self.menu = [Pizza("hawaiana", "pequeña", 10000),
                      Pizza("hawaiana", "mediana", 15000),
                      Pizza("hawaiana", "grande", 20000)]
        self.pedido=[]


    def mostrar_menu(self):
        print("/n--MENU--")
        for i in range(len(self.menu)):
            print(i+1, "nombre", self.menu[i][0],"tamaño", self.menu[i][1],
                   "precio", self.menu[i][2] )



    #def crear_pedido():

    #def mostrar_pedido
