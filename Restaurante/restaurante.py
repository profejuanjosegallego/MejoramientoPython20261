# Lista de usuarios registrados
usuarios = []

# Lista de ventas del restaurante
ventas_restaurante = [
    {"idVenta": 1,  "nombreCliente": "Carlos Perez",    "numeroMesa": 3,  "platoPrincipal": "Bandeja Paisa",       "valorConsumo": 32000, "metodoPago": "EFECTIVO",      "estadoPedido": "ENTREGADO"},
    {"idVenta": 2,  "nombreCliente": "Maria Lopez",     "numeroMesa": 1,  "platoPrincipal": "Ajiaco",              "valorConsumo": 25000, "metodoPago": "TARJETA",       "estadoPedido": "ENTREGADO"},
    {"idVenta": 3,  "nombreCliente": "Juan Torres",     "numeroMesa": 5,  "platoPrincipal": "Churrasco",           "valorConsumo": 48000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "PENDIENTE"},
    {"idVenta": 4,  "nombreCliente": "Ana Gomez",       "numeroMesa": 2,  "platoPrincipal": "Cazuela de Mariscos", "valorConsumo": 55000, "metodoPago": "TARJETA",       "estadoPedido": "ENTREGADO"},
    {"idVenta": 5,  "nombreCliente": "Luis Ramirez",    "numeroMesa": 7,  "platoPrincipal": "Pollo Asado",         "valorConsumo": 28000, "metodoPago": "EFECTIVO",      "estadoPedido": "PENDIENTE"},
    {"idVenta": 6,  "nombreCliente": "Sofia Herrera",   "numeroMesa": 4,  "platoPrincipal": "Trucha",              "valorConsumo": 38000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "ENTREGADO"},
    {"idVenta": 7,  "nombreCliente": "Andres Castro",   "numeroMesa": 6,  "platoPrincipal": "Costillas BBQ",       "valorConsumo": 62000, "metodoPago": "TARJETA",       "estadoPedido": "ENTREGADO"},
    {"idVenta": 8,  "nombreCliente": "Camila Vargas",   "numeroMesa": 8,  "platoPrincipal": "Sancocho",            "valorConsumo": 22000, "metodoPago": "EFECTIVO",      "estadoPedido": "PENDIENTE"},
    {"idVenta": 9,  "nombreCliente": "Diego Morales",   "numeroMesa": 3,  "platoPrincipal": "Lomo al Trapo",       "valorConsumo": 75000, "metodoPago": "TARJETA",       "estadoPedido": "ENTREGADO"},
    {"idVenta": 10, "nombreCliente": "Valentina Rios",  "numeroMesa": 2,  "platoPrincipal": "Arroz con Pollo",     "valorConsumo": 19000, "metodoPago": "EFECTIVO",      "estadoPedido": "PENDIENTE"},
]

# 2.   Función para registrar un nuevo usuario

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    correo = input("Correo: ").strip()

    for usuario in usuarios:
        if usuario["correo"] == correo:
            print("Ese correo ya está registrado.")
            return

    password = input("Password: ").strip()
    usuarios.append({"correo": correo, "password": password})
    print("Usuario registrado correctamente.")


def iniciar_sesion():
    print("\n--- INICIO DE SESION ---")
    max_intentos = 4

    for intento in range(max_intentos):
        correo   = input("Correo: ").strip()
        password = input("Password: ").strip()

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                print("Login exitoso. Bienvenido,", correo)
                return True

        intentos_restantes = max_intentos - (intento + 1)
        if intentos_restantes > 0:
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
        else:
            print("Cuenta bloqueada temporalmente.")
            return False

    return False

# 3. Funciones CRUD y ventas


def mostrar_ventas():
    print("\n--- VENTAS REGISTRADAS ---")
    if len(ventas_restaurante) == 0:
        print("No hay ventas registradas.")
        return
    for venta in ventas_restaurante:
        print(f"ID: {venta['idVenta']} | Cliente: {venta['nombreCliente']} | Mesa: {venta['numeroMesa']} | Plato: {venta['platoPrincipal']} | Valor: ${venta['valorConsumo']} | Pago: {venta['metodoPago']} | Estado: {venta['estadoPedido']}")


def ordenar_ventas():
    ventas_restaurante.sort(key=lambda venta: venta["valorConsumo"])
    print("\nVentas ordenadas por valor de menor a mayor.")
    mostrar_ventas()


def buscar_venta():
    print("\n--- BUSCAR VENTA ---")
    try:
        id_buscar = int(input("Ingrese el ID de la venta: "))
    except ValueError:
        print("ID no válido.")
        return

    for venta in ventas_restaurante:
        if venta["idVenta"] == id_buscar:
            print(f"\nVenta encontrada:")
            print(f"  Cliente : {venta['nombreCliente']}")
            print(f"  Mesa    : {venta['numeroMesa']}")
            print(f"  Plato   : {venta['platoPrincipal']}")
            print(f"  Valor   : ${venta['valorConsumo']}")
            print(f"  Pago    : {venta['metodoPago']}")
            print(f"  Estado  : {venta['estadoPedido']}")
            return

    print("No se encontró ninguna venta con ese ID.")


def eliminar_venta():
    print("\n--- ELIMINAR VENTA ---")
    try:
        id_eliminar = int(input("Ingrese el ID de la venta a eliminar: "))
    except ValueError:
        print("ID no válido.")
        return

    for venta in ventas_restaurante:
        if venta["idVenta"] == id_eliminar:
            ventas_restaurante.remove(venta)
            print(f"Venta {id_eliminar} eliminada correctamente.")
            return

    print("No se encontró ninguna venta con ese ID.")


def agregar_venta():
    print("\n--- AGREGAR VENTA ---")
    try:
        nuevo_id = int(input("ID de venta: "))
        nombre   = input("Nombre del cliente: ").strip()
        mesa     = int(input("Número de mesa: "))
        plato    = input("Plato principal: ").strip()
        valor    = float(input("Valor del consumo: "))

        metodo = input("Método de pago (EFECTIVO / TARJETA / TRANSFERENCIA): ").strip().upper()
        if metodo not in ["EFECTIVO", "TARJETA", "TRANSFERENCIA"]:
            print("Método de pago no válido.")
            return

        estado = input("Estado del pedido (ENTREGADO / PENDIENTE): ").strip().upper()
        if estado not in ["ENTREGADO", "PENDIENTE"]:
            print("Estado no válido.")
            return

        nueva_venta = {
            "idVenta"       : nuevo_id,
            "nombreCliente" : nombre,
            "numeroMesa"    : mesa,
            "platoPrincipal": plato,
            "valorConsumo"  : valor,
            "metodoPago"    : metodo,
            "estadoPedido"  : estado
        }

        ventas_restaurante.append(nueva_venta)
        print("Venta agregada correctamente.")

    except ValueError:
        print("Error: ingrese los datos en el formato correcto.")
        # ============================================================
# MENÚS
# ============================================================

def menu_ventas():
    while True:
        print("\n--- GESTIÓN DE VENTAS ---")
        print("1. Mostrar todas las ventas")
        print("2. Ordenar ventas por valor")
        print("3. Buscar venta por ID")
        print("4. Eliminar una venta")
        print("5. Agregar una venta")
        print("6. Volver")

        opcion = input("Seleccione una opción: ").strip()

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
            break
        else:
            print("Opción no válida.")


def menu_principal():
    while True:
        print("\n=============================")
        print("   RESTAURANTE - MENU PRINCIPAL")
        print("=============================")
        print("1. Gestionar ventas del restaurante")
        print("2. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_ventas()
        elif opcion == "2":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")

# Inicio del programa

print("=============================")
print("   RESTAURANTE - SISTEMA")
print("=============================")
print("1. Registrarse")
print("2. Iniciar sesión")

opcion_inicio = input("Seleccione una opción: ").strip()

if opcion_inicio == "1":
    registrar_usuario()
    sesion_activa = iniciar_sesion()
elif opcion_inicio == "2":
    sesion_activa = iniciar_sesion()
else:
    print("Opción no válida.")
    sesion_activa = False

if sesion_activa:
    menu_principal()