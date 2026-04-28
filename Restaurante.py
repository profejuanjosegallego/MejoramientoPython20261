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


