#mostrar menu
#crear pedido
#mostrar pedido

from metodos import Pizzeria
pizzeria = Pizzeria()
while True:
    print("Menu")
    opcion = int(input("ingrese una opcion"))
    #cantidad = int(input("ingrese una cantidad"))
    if opcion == "1":
        nombre = input("ingrese nombre del producto")
        posicion = buscar_por_nombre(matriz, nombre)
        if posicion is not None:
            print(posicion[o], posicion[1])
        else:
            print("nombre no valido")
        #hacer pedido

   # elif opcion == "2":
        #escoger cantidad

  #  elif opcion == "3":
        #salir

  #  else:
        print("opcion no valida")