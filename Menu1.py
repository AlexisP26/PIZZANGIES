from metodos import Pizzeria

pizzeria = Pizzeria()

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Buscar pizza por nombre")
    print("2. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese nombre de la pizza: ")

        posicion = pizzeria.buscar_pizza_por_nombre(nombre)

        if posicion is not None:
            fila, columna = posicion
            print("La pizza está en:")
            print("Fila:", fila)
            print("Columna:", columna)
        else:
            print("Pizza no encontrada")

    elif opcion == "2":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")