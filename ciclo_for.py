# Autor: David Francisco Castro Rocha


# 1. Ventas de un minisúper
def ventas():
    print("\n--- 1. Ventas de un minisúper ---")

    total = 0

    for dia in range(1, 8):
        print("Día", dia)

        venta = float(input("Ingrese la venta C$: "))

        total = total + venta

    promedio = total / 7

    print("Total semanal C$:", total)
    print("Promedio diario C$:", promedio)


# 2. Recepción de café
def cafe():
    print("\n--- 2. Recepción de café ---")

    total = 0

    for saco in range(1, 6):
        print("Saco número", saco)

        peso = float(input("Ingrese el peso en kg: "))

        total = total + peso

    print("Peso total recibido:", total, "kg")


# 3. Revisión de inventario
def inventario():
    print("\n--- 3. Revisión de inventario ---")

    contador = 0

    for producto in range(1, 9):
        print("\nProducto", producto)

        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad en existencia: "))

        if cantidad < 10:
            print(nombre, "tiene inventario bajo")

            contador = contador + 1

    print("Cantidad de alertas:", contador)


# 4. Producción de pan
def pan():
    print("\n--- 4. Producción de pan ---")

    total_producido = 0
    total_vendido = 0

    for dia in range(1, 7):
        print("\nDía", dia)

        producido = int(input("Cantidad producida: "))
        vendido = int(input("Cantidad vendida: "))

        total_producido = total_producido + producido
        total_vendido = total_vendido + vendido

    sobrante = total_producido - total_vendido

    print("Total producido:", total_producido)
    print("Total vendido:", total_vendido)
    print("Producto sobrante:", sobrante)


# 5. Evaluación del servicio
def servicio():
    print("\n--- 5. Evaluación del servicio ---")

    total = 0
    contador = 0

    for cliente in range(1, 11):
        print("Cliente", cliente)

        nota = int(input("Ingrese calificación de 1 a 5: "))

        total = total + nota

        if nota == 4 or nota == 5:
            contador = contador + 1

    promedio = total / 10

    print("Promedio:", promedio)
    print("Calificaciones de 4 o 5:", contador)