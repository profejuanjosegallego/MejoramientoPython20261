import random

usuarios = []  
opciones_pago = ["EFECTIVO", "TARJETA", "TRANSFERENCIA"]
platos_menu = ["Bandeja Paisa", "Ajiaco", "Cazuela de Mariscos", "Trucha al Ajillo", "Sancocho"]

ventas_restaurante = []
for i in range(1, 11):
    venta_inicial = {
        "idVenta": i,
        "nombreCliente": f"Cliente Genérico {i}",
        "numeroMesa": random.randint(1, 15),
        "platoPrincipal": random.choice(platos_menu),
        "valorConsumo": random.randint(20000, 90000),
        "metodoPago": random.choice(opciones_pago),
        "estadoPedido": "ENTREGADO"
    }
    ventas_restaurante.append(venta_inicial)


def registrar_usuario():
    print("\n--- REGISTRO DE NUEVO USUARIO ---")
    correo = input("Ingrese correo electrónico: ")
    password = input("Ingrese contraseña: ")
    usuarios.append({"correo": correo, "password": password})
    print("Usuario registrado exitosamente. ✅")

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    for intento in range(1, 5):
        correo_ing = input("Correo: ")
        pass_ing = input("Contraseña: ")
        
        for u in usuarios:
            if u["correo"] == correo_ing and u["password"] == pass_ing:
                print(f"\n¡Login exitoso! Bienvenido al sistema. 🔓")
                return True
        
        print(f"Credenciales incorrectas. Intentos restantes: {4 - intento}")
    
    print("\nCUENTA BLOQUEADA TEMPORALMENTE. 🚫")
    return False

def mostrar_ventas():
    print("\n--- LISTADO DE VENTAS ---")
    for v in ventas_restaurante:
      
        print(f"ID: {v['idVenta']} | Cliente: {v['nombreCliente']} | Total: ${v['valorConsumo']}")
    print("--------------------------")

def obtener_precio(venta):
    return venta["valorConsumo"]


def ordenar_ventas():
    ventas_restaurante.sort(key=obtener_precio)
    print("\nVentas ordenadas por valor de consumo (Menor a Mayor). 📈")
    mostrar_ventas()


def buscar_venta():
    try:
        id_buscado = int(input("\nIngrese el ID de la venta a buscar: "))
        for v in ventas_restaurante:
            if v["idVenta"] == id_buscado:
                print(f"\n✅ Venta encontrada:\n{v}")
                return
        print("❌ No se encontró ninguna venta con ese ID.")
    except ValueError:
        print("Error: Ingrese un número válido.")

def eliminar_venta():
    try:
        id_borrar = int(input("\nIngrese el ID de la venta a eliminar: "))
        for v in ventas_restaurante:
            if v["idVenta"] == id_borrar:
                ventas_restaurante.remove(v)
                print(f"Venta ID {id_borrar} eliminada correctamente. 🗑️")
                return
        print("❌ El ID especificado no existe.")
    except ValueError:
        print("Error: Ingrese un número válido.")

def registrar_venta():
    print("\n--- REGISTRAR NUEVA VENTA ---")    
    if ventas_restaurante:
        ids_actuales = [v["idVenta"] for v in ventas_restaurante]
        nuevo_id = max(ids_actuales) + 1
    else:
        nuevo_id = 1
    
    nombre = input("Nombre del cliente: ")
    mesa = int(input("Número de mesa: "))
    plato = input("Plato principal: ")
    valor = float(input("Valor del consumo: "))
    
  
    print("\nSeleccione el método de pago:")
    for i, metodo in enumerate(opciones_pago, 1):
        print(f"{i}. {metodo}")
    
    while True:
        try:
            opc = int(input("Elija una opción (1-3): "))
            if 1 <= opc <= len(opciones_pago):
                pago_final = opciones_pago[opc - 1]
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida.")

    nueva_v = {
        "idVenta": nuevo_id,
        "nombreCliente": nombre,
        "numeroMesa": mesa,
        "platoPrincipal": plato,
        "valorConsumo": valor,
        "metodoPago": pago_final,
        "estadoPedido": "PENDIENTE"
    }
    ventas_restaurante.append(nueva_v)
    print(f"¡Venta registrada con éxito! ID asignado: {nuevo_id} 🛒")

def ejecutar_programa():
    registrar_usuario()
    if iniciar_sesion():
        while True:
            print("\n--- MENÚ DE GESTIÓN ---")
            print("1. Ver todas las ventas")
            print("2. Ordenar por valor (Menor a Mayor)")
            print("3. Buscar venta por ID")
            print("4. Eliminar venta")
            print("5. Registrar nueva venta")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1": mostrar_ventas()
            elif opcion == "2": ordenar_ventas()
            elif opcion == "3": buscar_venta()
            elif opcion == "4": eliminar_venta()
            elif opcion == "5": registrar_venta()
            elif opcion == "6":
                print("Cerrando sistema... ¡Hasta pronto! 👋")
                break
            else:
                print("Opción no válida.")

ejecutar_programa()


