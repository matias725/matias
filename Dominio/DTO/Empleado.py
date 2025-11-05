class Empleado:
    def __init__(self, id_empleado=None, run="", nombre="", apellidos="", 
                 direccion="", fono="", correo="", fecha_contrato=None, id_departamento=None):
        self.id_empleado = id_empleado
        self.run = run
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.fono = fono
        self.correo = correo
        self.fecha_contrato = fecha_contrato
        self.id_departamento = id_departamento

    def __str__(self):
        return f"ID: {self.id_empleado}, RUN: {self.run}, Nombre: {self.nombre} {self.apellidos}, Departamento: {self.id_departamento}"