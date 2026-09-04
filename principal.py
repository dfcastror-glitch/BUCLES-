# Autor: David Francisco Castro Rocha

import ciclo_for
import ciclo_while


def menu():
    opcion = 0

    while opcion != 11:

        print("\n===== MENÚ GENERAL DE BUCLES =====")
        print("1. Ventas de un minisúper")
        print("2. Recepción de café")
        print("3. Revisión de inventario")
        print("4. Producción de pan")
        print("5. Evaluación del servicio")
        print("6. Cierre de caja")
        print("7. Acceso al sistema")
        print("8. Cantidad de un pedido")
        print("9. Combustible de reparto")
        print("10. Reposición de existencias")
        print("11. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ciclo_for.ventas()

        elif opcion == 2:
            ciclo_for.cafe()

        elif opcion == 3:
            ciclo_for.inventario()

        elif opcion == 4:
            ciclo_for.pan()

        elif opcion == 5:
            ciclo_for.servicio()

        elif opcion == 6:
            ciclo_while.caja()

        elif opcion == 7:
            ciclo_while.acceso()

        elif opcion == 8:
            ciclo_while.pedido()

        elif opcion == 9:
            ciclo_while.combustible()

        elif opcion == 10:
            ciclo_while.reposicion()

        elif opcion == 11:
            print("Programa finalizado")

        else:
            print("Opción no válida")


menu()