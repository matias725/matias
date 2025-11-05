from Presentacion.MenuBase import MenuBase
from Dominio.DTO.Proyecto import Proyecto
from Aplicacion import ReglasProyecto

class MenuProyecto(MenuBase):
    def __init__(self):
        super().__init__("Gestión de Proyectos")
    
    def agregar(self):
        print("\n--- Agregar Proyecto ---")
        nombre = input("Nombre del proyecto: ")
        fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
        id_director = int(input("ID del director (empleado): "))
        
        proyecto = Proyecto(nombre=nombre, fecha_inicio=fecha_inicio, id_director=id_director)
        
        if ReglasProyecto.agregar(proyecto):
            print("Proyecto agregado exitosamente")
    
    def mostrarTodos(self):
        print("\n--- Lista de Proyectos ---")
        proyectos = ReglasProyecto.mostrarTodos()
        if proyectos:
            for proy in proyectos:
                print(proy)
        else:
            print("No hay proyectos registrados")
    
    def buscarPorCodigo(self):
        print("\n--- Buscar Proyecto por ID ---")
        id_proy = int(input("ID del proyecto: "))
        proyecto = ReglasProyecto.buscarPorCodigo(id_proy)
        if proyecto:
            print(proyecto)
        else:
            print("Proyecto no encontrado")
    
    def buscarPorNombre(self):
        print("\n--- Buscar Proyecto por Nombre ---")
        nombre = input("Nombre del proyecto: ")
        proyectos = ReglasProyecto.buscarPorNombre(nombre)
        if proyectos:
            for proy in proyectos:
                print(proy)
        else:
            print("No se encontraron proyectos")
    
    def modificar(self):
        print("\n--- Modificar Proyecto ---")
        id_proy = int(input("ID del proyecto a modificar: "))
        proyecto = ReglasProyecto.buscarPorCodigo(id_proy)
        if proyecto:
            print(f"Proyecto actual: {proyecto}")
            proyecto.nombre = input(f"Nombre ({proyecto.nombre}): ") or proyecto.nombre
            proyecto.fecha_inicio = input(f"Fecha inicio ({proyecto.fecha_inicio}): ") or proyecto.fecha_inicio
            proyecto.id_director = int(input(f"ID Director ({proyecto.id_director}): ") or proyecto.id_director)
            
            if ReglasProyecto.modificar(proyecto):
                print("Proyecto modificado exitosamente")
        else:
            print("Proyecto no encontrado")
    
    def eliminar(self):
        print("\n--- Eliminar Proyecto ---")
        id_proy = int(input("ID del proyecto a eliminar: "))
        proyecto = ReglasProyecto.buscarPorCodigo(id_proy)
        if proyecto:
            print(f"Proyecto a eliminar: {proyecto}")
            confirmacion = input("¿Está seguro? (s/n): ")
            if confirmacion.lower() == 's':
                if ReglasProyecto.eliminar(id_proy):
                    print("Proyecto eliminado exitosamente")
        else:
            print("Proyecto no encontrado")