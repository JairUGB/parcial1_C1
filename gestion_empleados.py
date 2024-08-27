# Clase base para todos los empleados
class Empleado:
    def __init__(self, nombre, anios_trabajados):
        self.nombre = nombre  # Nombre del empleado
        self.anios_trabajados = anios_trabajados  # Años trabajados en la empresa

    # Método para calcular el pago, debe ser implementado por las subclases
    def calcular_pago(self):
        raise NotImplementedError("Debe implementar este método en las subclases")

    # Método para calcular el bono adicional si el empleado ha trabajado más de 5 años
    def calcular_bono(self):
        if self.anios_trabajados > 5:
            return 500  # Bono adicional para empleados con más de 5 años
        return 0

# Clase para empleados con plaza fija
class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, anios_trabajados, salario_base, comisiones):
        super().__init__(nombre, anios_trabajados)  # Inicializa los atributos heredados
        self.salario_base = salario_base  # Salario base mensual
        self.comisiones = comisiones  # Comisiones adicionales

    # Calcula el pago total sumando el salario base, comisiones y el bono
    def calcular_pago(self):
        return self.salario_base + self.comisiones + self.calcular_bono()

# Clase para empleados que trabajan por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, anios_trabajados, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre, anios_trabajados)  # Inicializa los atributos heredados
        self.tarifa_por_hora = tarifa_por_hora  # Tarifa por hora trabajada
        self.horas_trabajadas = horas_trabajadas  # Número de horas trabajadas

    # Calcula el pago total en función de la tarifa por hora, horas trabajadas y el bono
    def calcular_pago(self):
        return (self.tarifa_por_hora * self.horas_trabajadas) + self.calcular_bono()

# Función principal para gestionar la planilla de pago
def main():
    # Crear una lista de 2 empleados con datos ya registrados
    empleados = [
        EmpleadoPlazaFija("Juan Pérez", 6, 2000, 300),
        EmpleadoPorHoras("Luis Ramírez", 7, 15, 160)
    ]

    # Imprimir encabezado de la planilla de pago
    print("--- Planilla de Pago ---")
    # Iterar sobre cada empleado para calcular y mostrar el pago total
    for empleado in empleados:
        nombre = empleado.nombre  # Nombre del empleado
        pago_total = empleado.calcular_pago()  # Calcular el total a pagar
        print(f"Empleado: {nombre}")
        print(f"Total a pagar: ${pago_total}\n")

    # Aquí puedes agregar más empleados si lo deseas
    while True:
        agregar = input("¿Desea agregar otro empleado? (si/no): ").strip().lower()
        if agregar == "no":
            break
        tipo = input("Ingrese el tipo de empleado (fijo/horas): ").strip().lower()
        nombre = input("Ingrese el nombre del empleado: ").strip()
        anios_trabajados = int(input("Ingrese los años trabajados: ").strip())

        if tipo == "fijo":
            salario_base = float(input("Ingrese el salario base: ").strip())
            comisiones = float(input("Ingrese las comisiones: ").strip())
            empleados.append(EmpleadoPlazaFija(nombre, anios_trabajados, salario_base, comisiones))
        elif tipo == "horas":
            tarifa_por_hora = float(input("Ingrese la tarifa por hora: ").strip())
            horas_trabajadas = int(input("Ingrese el número de horas trabajadas: ").strip())
            empleados.append(EmpleadoPorHoras(nombre, anios_trabajados, tarifa_por_hora, horas_trabajadas))

    # Imprimir la planilla actualizada si se agregaron nuevos empleados
    print("--- Planilla de Pago Actualizada ---")
    for empleado in empleados:
        nombre = empleado.nombre
        pago_total = empleado.calcular_pago()
        print(f"Empleado: {nombre}")
        print(f"Total a pagar: ${pago_total}\n")

if __name__ == "__main__":
    main()