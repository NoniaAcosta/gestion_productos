import os

productos = []


def añadir_producto():
    print("Por favor, introduzca el nombre del producto:")
    nombre_producto = input()
    while True:
        print("Por favor, introduzca el precio:")
        precio = input()
        if not precio.isdigit():  # Verificar si es un número entero
            print("El precio debe ser un numerico")
        else:
            break

    # Validar la cantidad
    while True:
        print("Por favor, introduzca la cantidad:")
        cantidad = input()
        if cantidad.isdigit():
            break  # Salir del bucle si la cantidad es válida
        else:
            print("La cantidad debe ser numerico.")
    productos.append(
        {"producto": nombre_producto, "cantidad": cantidad, "precio": precio},
    )


def ver_productos():
    for producto in productos:
        print(
            f"Producto: {producto['producto']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}"
        )


def actualizar_producto():
    print("¿Qué producto desea editar? ")
    print("-----Lista de Productos-----")
    ver_productos()  # Mostrar los productos disponibles
    producto_a_editar = input(
        "Ingrese el nombre: "
    ).strip()  # Eliminar espacios alrededor

    # Verificar si el producto existe
    producto_encontrado = False
    for producto in productos:
        if producto_a_editar == producto["producto"]:
            producto_encontrado = True
            print(f"Producto encontrado: {producto_a_editar}")

            # Solicitar nuevos datos
            print("Ingrese nuevo nombre:")
            producto_editado = input().strip()

            print("Ingrese nuevo precio:")
            precio_editado = input().strip()
            precio_editado = (
                float(precio_editado) if "." in precio_editado else int(precio_editado)
            )

            print("Ingrese nueva cantidad:")
            cantidad_editada = int(input().strip())

            # Actualizar los valores en el diccionario del producto
            producto["producto"] = producto_editado
            producto["precio"] = precio_editado
            producto["cantidad"] = cantidad_editada

            print(f"Producto actualizado: {producto_editado}")
            break

    if not producto_encontrado:
        print(f"El producto '{producto_a_editar}' no se encontró.")


def eliminar_producto():
    print("¿Qué producto desea eliminar? ")
    ver_productos()  # Mostrar los productos disponibles
    producto_a_eliminar = input("Ingrese el nombre: ").strip()
    for producto in productos:
        if producto["producto"] == producto_a_eliminar:
            productos.remove(producto)
            print(f"Producto eliminado.")
            return
    print("-----Lista Actualizada-----")
    ver_productos()


def guardar_datos():
    with open("productos.txt", "w") as file_pc:  # Usa "with" para abrir el archivo
        for producto in productos:
            print(producto)
            # Formatear la cadena
            post = (
                f"{producto['producto']},{producto['precio']},{producto['cantidad']}\n"
            )
            file_pc.write(f"{post}")
    print("-----Datos Actualizados-----")


def cargar_datos():
    if os.path.exists("productos.txt"):
        print("---Listado de produtos---")
        file_pc = open("productos.txt", "r")
        contenido = file_pc.readlines()
        for linea in contenido:
            if linea.strip():  # Ignora líneas vacías
                # Extrae los valores de la línea actual
                datos = linea.strip().split(",")
                producto = {
                    "producto": datos[0],
                    "precio": (datos[1]),
                    "cantidad": (datos[2]),
                }
                productos.append(producto)


def menu():
    print("Operaciones posibles a realizar")
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        opcion = input("Selecciona una opción: ")
        if opcion.isdecimal():
            opcion = int(opcion)
            if opcion == 1:
                añadir_producto()
            elif opcion == 2:
                ver_productos()
            elif opcion == 3:
                actualizar_producto()
            elif opcion == 4:
                eliminar_producto()
            elif opcion == 5:
                guardar_datos()
                break
            else:
                print("Por favor, selecciona una opción válida.")
        else:
            print("Por favor, ingrese numeros de 1 al 5")


cargar_datos()
ver_productos()
menu()
