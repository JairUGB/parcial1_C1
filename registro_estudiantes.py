class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = []

    def registrar_asistencia(self, estado, fecha, razon=None):
        asistencia = {
            'fecha': fecha,
            'estado': estado,
            'razon': razon
        }
        self.asistencias.append(asistencia)

class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)

    def registrar_asistencia(self):
        fecha = input("Ingrese la fecha de hoy (YYYY-MM-DD): ")
        for estudiante in self.lista_estudiantes:
            print(f"\nRegistrando asistencia para {estudiante.nombre}:")
            estado = input("¿Asistió? (s/n): ").strip().lower()
            if estado == "s":
                estudiante.registrar_asistencia("Asistió", fecha)
            elif estado == "n":
                tipo_falta = input("¿Es una inasistencia o tiene permiso? (inasistencia/permiso): ").strip().lower()
                if tipo_falta == "permiso":
                    razon = input("Ingrese la razón del permiso: ")
                    estudiante.registrar_asistencia("Permiso", fecha, razon)
                else:
                    estudiante.registrar_asistencia("Inasistencia", fecha)
            else:
                print("Entrada no válida, intente de nuevo.")

    def generar_reporte(self):
        reporte = {}
        for estudiante in self.lista_estudiantes:
            reporte[estudiante.nombre] = estudiante.asistencias
        return reporte

# Crear docente
docente = Docente("Profesor Jair")

# Agregar 10 estudiantes
nombres_estudiantes = [
    "Pedro Pascal", "Ana de Armas", "Luis Díaz", "María Becerra",
    "José Martínez", "Carmen Torres", "Raúl Vásquez", "Elena White",
    "Miguel Luis", "Sofía Vergara"
]

for nombre in nombres_estudiantes:
    docente.agregar_estudiante(Estudiante(nombre))

# Registrar asistencias
docente.registrar_asistencia()

# Generar y mostrar reporte
reporte = docente.generar_reporte()
print("\n--- Reporte de Asistencia ---")
for estudiante, asistencias in reporte.items():
    print(f"Estudiante: {estudiante}")
    for asistencia in asistencias:
        print(f"  Fecha: {asistencia['fecha']}, Estado: {asistencia['estado']}, Razón: {asistencia['razon']}")