class Habitacion:
    def __init__(self, tipo, precio_noche):
        self.tipo = tipo
        self.precio_noche = precio_noche

class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.numero_noches = 0
        self.habitacion = None
        self.servicios_extra = []

    def seleccionar_habitacion(self, habitacion):
        self.habitacion = habitacion

    def agregar_servicio_extra(self, servicio):
        self.servicios_extra.append(servicio)

    def calcular_total(self):
        total = self.habitacion.precio_noche * self.numero_noches
        total += sum(servicio['precio'] for servicio in self.servicios_extra)
        return total

    def generar_factura(self):
        factura = f"Factura para {self.nombre} ({self.dni})\n"
        factura += f"Habitación: {self.habitacion.tipo} - Precio por noche: ${self.habitacion.precio_noche}\n"
        factura += f"Número de noches: {self.numero_noches}\n"
        factura += f"Total por habitación: ${self.habitacion.precio_noche * self.numero_noches}\n"
        factura += "Servicios extra:\n"
        for servicio in self.servicios_extra:
            factura += f"  {servicio['nombre']} - ${servicio['precio']}\n"
        factura += f"Total a pagar: ${self.calcular_total()}\n"
        return factura

class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.servicios_extra = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def agregar_servicio_extra(self, nombre, precio):
        self.servicios_extra.append({'nombre': nombre, 'precio': precio})

    def mostrar_habitaciones(self):
        print("Opciones de habitaciones disponibles:")
        for i, habitacion in enumerate(self.habitaciones):
            print(f"{i + 1}. {habitacion.tipo} - Precio por noche: ${habitacion.precio_noche}")

    def mostrar_servicios_extra(self):
        print("Servicios extra disponibles:")
        for i, servicio in enumerate(self.servicios_extra):
            print(f"{i + 1}. {servicio['nombre']} - Precio: ${servicio['precio']}")

def main():
    # Crear hotel
    hotel = Hotel()

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion("Suite con vista al mar", 150))
    hotel.agregar_habitacion(Habitacion("Habitación estándar", 100))

    # Agregar servicios extra
    hotel.agregar_servicio_extra("Uso de la piscina", 20)
    hotel.agregar_servicio_extra("Acceso a la cancha de golf", 50)

    # Mostrar habitaciones y servicios extra
    hotel.mostrar_habitaciones()
    hotel.mostrar_servicios_extra()

    # Solicitar datos del cliente
    nombre = input("Ingrese el nombre del cliente: ")
    dni = input("Ingrese el DUI del cliente: ")
    cliente = Cliente(nombre, dni)

    # Selección de habitación
    seleccion_habitacion = int(input("Seleccione el número de habitación: ")) - 1
    cliente.seleccionar_habitacion(hotel.habitaciones[seleccion_habitacion])

    # Número de noches
    cliente.numero_noches = int(input("Ingrese el número de noches de estancia: "))

    # Selección de servicios extra
    while True:
        seleccion_servicio = input("¿Desea agregar un servicio extra? (s/n): ").strip().lower()
        if seleccion_servicio == "n":
            break
        hotel.mostrar_servicios_extra()
        servicio_seleccionado = int(input("Seleccione el número del servicio extra: ")) - 1
        cliente.agregar_servicio_extra(hotel.servicios_extra[servicio_seleccionado])

    # Generar y mostrar factura
    factura = cliente.generar_factura()
    print("\n--- Factura ---")
    print(factura)

if __name__ == "__main__":
    main()
