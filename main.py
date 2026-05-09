usuarios = []
ventas = [
    {
        "id": 1,
        "cliente": "Carlos",
        "producto": "Hamburguesa",
        "cantidad": 2,
        "total": 30000
    },
    {
        "id": 2,
        "cliente": "Laura",
        "producto": "Pizza",
        "cantidad": 1,
        "total": 25000
    },
    {
        "id": 3,
        "cliente": "Miguel",
        "producto": "Perro",
        "cantidad": 3,
        "total": 27000
    },
    {
        "id": 4,
        "cliente": "Sofia",
        "producto": "Salchipapa",
        "cantidad": 1,
        "total": 18000
    },
    {
        "id": 5,
        "cliente": "Juan",
        "producto": "Tacos",
        "cantidad": 2,
        "total": 22000
    },
    {
        "id": 6,
        "cliente": "Valentina",
        "producto": "Empanadas",
        "cantidad": 5,
        "total": 15000
    },
    {
        "id": 7,
        "cliente": "Camilo",
        "producto": "Gaseosa",
        "cantidad": 2,
        "total": 8000
    },
    {
        "id": 8,
        "cliente": "Andres",
        "producto": "Helado",
        "cantidad": 4,
        "total": 20000
    },
    {
        "id": 9,
        "cliente": "Daniela",
        "producto": "Arepa",
        "cantidad": 3,
        "total": 12000
    },
    {
        "id": 10,
        "cliente": "Mateo",
        "producto": "Jugo",
        "cantidad": 2,
        "total": 10000
    }
]


def registrar_usuario():
    print("\n--- REGISTRO ---")

    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")

    nuevo_usuario = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    usuarios.append(nuevo_usuario)

    print("Usuario registrado correctamente")



def iniciar_sesion():
    print("\n--- LOGIN ---")

    intentos = 4

    while intentos > 0:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        for dato in usuarios:
            if dato["usuario"] == usuario and dato["contraseña"] == contraseña:
                print("Inicio de sesión exitoso")
                return True

        intentos -= 1
        print("Datos incorrectos")
        print("Intentos restantes:", intentos)

    print("Cuenta bloqueada")
    return False



def mostrar_ventas():
    print("\n--- LISTA DE VENTAS ---")

    for venta in ventas:
        print(venta)



def ordenar_ventas():
    print("\n--- ORDENAR VENTAS ---")

    ventas_ordenadas = sorted(ventas, key=lambda venta: venta["total"])

    for venta in ventas_ordenadas:
        print(venta)



def buscar_venta():
    print("\n--- BUSCAR VENTA ---")

    id_buscar = int(input("Ingrese ID de la venta: "))

    for venta in ventas:
        if venta["id"] == id_buscar:
            print("Venta encontrada")
            print(venta)
            return

    print("Venta no encontrada")



def eliminar_venta():
    print("\n--- ELIMINAR VENTA ---")

    id_eliminar = int(input("Ingrese ID a eliminar: "))

    for venta in ventas:
        if venta["id"] == id_eliminar:
            ventas.remove(venta)
            print("Venta eliminada")
            return

    print("No existe la venta")



def agregar_venta():
    print("\n--- AGREGAR VENTA ---")

    id_venta = int(input("Ingrese ID: "))
    cliente = input("Ingrese cliente: ")
    producto = input("Ingrese producto: ")
    cantidad = int(input("Ingrese cantidad: "))
    total = int(input("Ingrese total: "))

    nueva_venta = {
        "id": id_venta,
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad,
        "total": total
    }

    ventas.append(nueva_venta)

    print("Venta agregada correctamente")



def menu():
    while True:
        print("\n====== MENU ======")
        print("1. Mostrar ventas")
        print("2. Ordenar ventas")
        print("3. Buscar venta")
        print("4. Eliminar venta")
        print("5. Agregar venta")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_ventas()

        elif opcion == "2":
            ordenar_ventas()

        elif opcion == "3":
            buscar_venta()

        elif opcion == "4":
            eliminar_venta()

        elif opcion == "5":
            agregar_venta()

        elif opcion == "6":
            print("Saliendo del sistema")
            break

        else:
            print("Opción inválida")


registrar_usuario()

acceso = iniciar_sesion()

if acceso:
    menu()