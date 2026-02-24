
pizzeria = Pizzeria()

while True:
    print("\n=== PIZZERIA ===")
    print("1) Crear pedido")
    print("2) Mostrar pedidos")
    print("3) Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        pizzeria.crear_pedido()

    elif opcion == "2":
        pizzeria.mostrar_pedidos()

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")