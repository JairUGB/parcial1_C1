class Tienda:
    def vender_producto(self):
        # Ingresar detalles del producto
        nombre = input("Ingrese el nombre del producto: ")
        precio_venta = float(input(f"Ingrese el precio de venta de {nombre}: "))
        cantidad = int(input(f"Ingrese la cantidad de {nombre} que se va a vender: "))
        
        # Calcular el total de la venta
        total_venta = precio_venta * cantidad
        
        # Ingresar el pago del cliente
        pago = float(input("Ingrese el pago del cliente: "))
        
        # Calcular el vuelto
        if pago >= total_venta:
            vuelto = pago - total_venta
            return f"Total: {total_venta}, Vuelto: {vuelto}"
        else:
            return "El pago no es suficiente para cubrir el total de la compra."

# Ejemplo de uso
tienda = Tienda()

# Realizar la venta
resultado = tienda.vender_producto()
print(resultado)
