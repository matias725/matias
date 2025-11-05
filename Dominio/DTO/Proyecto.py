class Proyecto:
    def __init__(self, id_proyecto=None, nombre="", fecha_inicio=None, id_director=None):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.id_director = id_director

    def __str__(self):
        return f"ID: {self.id_proyecto}, Nombre: {self.nombre}, Director: {self.id_director}"