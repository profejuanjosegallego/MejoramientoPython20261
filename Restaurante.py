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
