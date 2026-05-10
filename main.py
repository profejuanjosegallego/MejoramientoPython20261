usuarios = []

ventas_restaurante = []


ventas_restaurante = [

    {
        "idVenta": 1,
        "nombreCliente": "Juan",
        "numeroMesa": 3,
        "platoPrincipal": "Hamburguesa",
        "valorConsumo": 35000,
        "metodoPago": "TARJETA",
        "estadoPedido": "ENTREGADO"
    },

    {
        "idVenta": 2,
        "nombreCliente": "Maria",
        "numeroMesa": 5,
        "platoPrincipal": "Pizza",
        "valorConsumo": 50000,
        "metodoPago": "EFECTIVO",
        "estadoPedido": "PENDIENTE"
    },

    {
        "idVenta": 3,
        "nombreCliente": "Carlos",
        "numeroMesa": 1,
        "platoPrincipal": "Perro Caliente",
        "valorConsumo": 20000,
        "metodoPago": "TRANSFERENCIA",
        "estadoPedido": "ENTREGADO"
    },

    {
        "idVenta": 4,
        "nombreCliente": "Laura",
        "numeroMesa": 4,
        "platoPrincipal": "Bandeja Paisa",
        "valorConsumo": 45000,
        "metodoPago": "TARJETA",
        "estadoPedido": "ENTREGADO"
    },

    {
        "idVenta": 5,
        "nombreCliente": "Andres",
        "numeroMesa": 6,
        "platoPrincipal": "Tacos",
        "valorConsumo": 30000,
        "metodoPago": "EFECTIVO",
        "estadoPedido": "PENDIENTE"
    },

    {
        "idVenta": 6,
        "nombreCliente": "Sofia",
        "numeroMesa": 2,
        "platoPrincipal": "Sushi",
        "valorConsumo": 60000,
        "metodoPago": "TRANSFERENCIA",
        "estadoPedido": "ENTREGADO"
    },

    {
        "idVenta": 7,
        "nombreCliente": "David",
        "numeroMesa": 8,
        "platoPrincipal": "Pasta",
        "valorConsumo": 38000,
        "metodoPago": "TARJETA",
        "estadoPedido": "PENDIENTE"
    },

    {
        "idVenta": 8,
        "nombreCliente": "Valentina",
        "numeroMesa": 7,
        "platoPrincipal": "Ensalada",
        "valorConsumo": 25000,
        "metodoPago": "EFECTIVO",
        "estadoPedido": "ENTREGADO"
    },

    {
        "idVenta": 9,
        "nombreCliente": "Mateo",
        "numeroMesa": 9,
        "platoPrincipal": "Pollo Asado",
        "valorConsumo": 42000,
        "metodoPago": "TRANSFERENCIA",
        "estadoPedido": "PENDIENTE"
    },

    {
        "idVenta": 10,
        "nombreCliente": "Camila",
        "numeroMesa": 10,
        "platoPrincipal": "Arepa Burger",
        "valorConsumo": 33000,
        "metodoPago": "TARJETA",
        "estadoPedido": "ENTREGADO"
    }

]


def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")

    correo = input("Ingrese su correo: ")
    password = input("Ingrese su contraseña: ")

    usuario = {
        "correo": correo,
        "password": password
    }

    usuarios.append(usuario)

    print("Usuario registrado correctamente")


def login():

    intentos = 4

    while intentos > 0:

        print("\n--- LOGIN ---")

        correo = input("Correo: ")
        password = input("Password: ")

        for usuario in usuarios:

            if usuario["correo"] == correo and usuario["password"] == password:
                print("Login exitoso")
                return True

        intentos -= 1

        print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

    print("Cuenta bloqueada temporalmente")
    return False


def mostrar_ventas():

    print("\n--- LISTA DE VENTAS ---")

    for venta in ventas_restaurante:
        print(venta)


def ordenar_ventas():

    ventas_restaurante.sort(key=lambda venta: venta["valorConsumo"])

    print("\nVentas ordenadas correctamente")


def buscar_venta():

    id_buscar = int(input("Ingrese el id de la venta: "))

    for venta in ventas_restaurante:

        if venta["idVenta"] == id_buscar:
            print(venta)
            return

    print("Venta no encontrada")


def eliminar_venta():

    id_eliminar = int(input("Ingrese el id de la venta a eliminar: "))

    for venta in ventas_restaurante:

        if venta["idVenta"] == id_eliminar:
            ventas_restaurante.remove(venta)
            print("Venta eliminada correctamente")
            return

    print("Venta no encontrada")


def agregar_venta():

    id_venta = int(input("Ingrese el id: "))
    nombre = input("Ingrese nombre del cliente: ")
    mesa = int(input("Ingrese número de mesa: "))
    plato = input("Ingrese plato principal: ")
    valor = float(input("Ingrese valor del consumo: "))
    metodo = input("Ingrese método de pago: ")
    estado = input("Ingrese estado del pedido: ")

    nueva_venta = {
        "idVenta": id_venta,
        "nombreCliente": nombre,
        "numeroMesa": mesa,
        "platoPrincipal": plato,
        "valorConsumo": valor,
        "metodoPago": metodo,
        "estadoPedido": estado
    }

    ventas_restaurante.append(nueva_venta)

    print("Venta agregada correctamente")

registrar_usuario()

acceso = login()

if acceso:

    while True:

        print("\n--- MENÚ PRINCIPAL ---")
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
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")