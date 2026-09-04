# Autor: David Francisco Castro Rocha


# 1. Cierre de caja
def caja():
    print("\n--- 1. Cierre de caja ---")

    total = 0
    contador = 0

    venta = float(input("Ingrese una venta o 0 para terminar: "))

    while venta != 0:

        total = total + venta
        contador = contador + 1

        venta = float(input("Ingrese otra venta o 0 para terminar: "))

    print("Total recaudado C$:", total)
    print("Cantidad de ventas:", contador)


# 2. Acceso al sistema
def acceso():
    print("\n--- 2. Acceso al sistema ---")

    clave_correcta = "1234"
    clave = ""
    intentos = 0

    while clave != clave_correcta:

        clave = input("Ingrese la clave: ")

        intentos = intentos + 1

        if clave != clave_correcta:
            print("Clave incorrecta")

    print("Clave correcta")
    print("Intentos realizados:", intentos)


# 3. Cantidad de un pedido
def pedido():
    print("\n--- 3. Cantidad de un pedido ---")

    cantidad = int(input("Ingrese la cantidad: "))

    while cantidad < 1 or cantidad > 100:

        print("Cantidad no válida")

        cantidad = int(input("Ingrese una cantidad entre 1 y 100: "))

    precio = float(input("Precio por unidad C$: "))

    total = cantidad * precio

    print("Cantidad aceptada:", cantidad)
    print("Total a pagar C$:", total)


# 4. Combustible de reparto
def combustible():
    print("\n--- 4. Combustible de reparto ---")

    litros = 8

    print("Combustible inicial:", litros, "litros")

    while litros > 1:

        consumo = float(input("Consumo del recorrido: "))

        litros = litros - consumo

        if litros < 0:
            litros = 0

        print("Combustible disponible:", litros, "litros")

    print("Alerta: combustible bajo")


# 5. Reposición de existencias
def reposicion():
    print("\n--- 5. Reposición de existencias ---")

    existencia = 3

    print("Existencia inicial:", existencia)

    while existencia < 20:

        cantidad = int(input("Cantidad a reponer: "))

        if cantidad <= 0:
            print("Cantidad no válida")

        else:
            existencia = existencia + cantidad

            print("Existencia actual:", existencia)

    print("Meta alcanzada")