productos = {}

def añadir_producto():    
    print('Por favor, introduzca el nombre del producto:')
    nombre_producto = input()

    # Verifica si el producto ya existe
    if nombre_producto in productos:
        print("Este producto ya existe. Intente con otro nombre.")
        return  # Salir de la función si el producto ya existe

    # Crear un diccionario para las propiedades del producto
    producto_info = {}

    # Validar el precio
    while True:
        print('Por favor, introduzca el precio:')
        precio = input()
        if precio.isdigit():  # Verificar si es un número entero
            producto_info['precio'] = int(precio)  # Asignar el precio al diccionario
            break  # Salir del bucle si el precio es válido
        else:
            print("El precio debe ser un numerico")
    
    # Validar la cantidad
    while True:
        print('Por favor, introduzca la cantidad:')
        cantidad = input()
        if cantidad.isdigit():  
            producto_info['cantidad'] = int(cantidad)  # Asignar la cantidad al diccionario
            break  # Salir del bucle si la cantidad es válida
        else:
            print("La cantidad debe ser numerico.")

    # Agregar el producto al diccionario
    productos[nombre_producto] = producto_info
    print(f"Producto '{nombre_producto}' añadido exitosamente.")


def ver_productos():
    for producto, detalles in productos.items():
        print(f"Producto: {producto}")
        for atributo, valor in detalles.items():
            print(f"  {atributo}: {valor}")

def actualizar_producto():
    print("¿Qué producto desea editar? ")
    print("-----Lista de Productos-----") 
    ver_productos()  # Mostrar los productos disponibles
    producto_a_editar = input("Ingrese el nombre: ").strip()  # Eliminar espacios alrededor

    # Verificar si el producto existe
    if producto_a_editar in productos:
        print(f"Producto encontrado: {producto_a_editar}")
        
        # Solicitar nuevos datos
        print("Ingrese nuevo nombre:")
        producto_editado = input().strip()

        print("Ingrese nuevo precio:")
        precio_editado = input().strip()

        print("Ingrese nueva cantidad:")
        cantidad_editada = input().strip()

        # Si el nombre del producto cambia, usa pop para eliminarlo y asignar el nuevo
        if producto_a_editar != producto_editado:
            productos[producto_editado] = productos.pop(producto_a_editar)  # Cambiar nombre
        # Actualizar el precio y la cantidad
        productos[producto_editado]['precio'] = precio_editado
        productos[producto_editado]['cantidad'] = cantidad_editada
        
        print(f"Producto actualizado: {producto_editado}")
    else:
        print(f"El producto '{producto_a_editar}' no se encontró.")
    print("-----Lista Actualizada-----") 
    ver_productos()    

def eliminar_producto():
    print("¿Qué producto desea eliminar? ")
    ver_productos()  # Mostrar los productos disponibles
    producto_a_eliminar = input("Ingrese el nombre: ").strip()
    del(productos[producto_a_eliminar])
    print("-----Lista Actualizada-----") 
    ver_productos()

def guardar_datos():
    file_pc = open("productos.txt", 'a')
    for producto, detalles in productos.items():
   # Formatear la cadena como desees
        post = f'Producto: {producto}, Precio: {detalles["precio"]}, Cantidad: {detalles["cantidad"]}\n'
        file_pc.write(f'{ post } \n')
    file_pc.close()
    print("-----Datos Actualizados-----")

def cargar_datos():
    print("---Listado de produtos---")
    file_pc=open("productos.txt", 'r')  
    contenido = file_pc.readlines()  
    for linea in contenido:
        print(linea.strip())

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
            opcion=int(opcion)
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
menu()