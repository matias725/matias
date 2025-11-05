class Departamento:
    def __init__(self, id_departamento=None, nombre=""):
        self.id_departamento = id_departamento
        self.nombre = nombre

    def __str__(self):
        return f"ID: {self.id_departamento}, Nombre: {self.nombre}"