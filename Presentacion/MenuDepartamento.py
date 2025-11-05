from Presentacion.MenuBase import MenuBase
from Dominio.DTO.Departamento import Departamento
from Aplicacion import ReglasDepartamento

class MenuDepartamento(MenuBase):
    def __init__(self):
        super().__init__("Gestión de Departamentos")
    
    def agregar(self):
        print("\n--- Agregar Departamento ---")
        nombre = input("Nombre del departamento: ")
        departamento = Departamento(nombre=nombre)
        
        if ReglasDepartamento.agregar(departamento):
            print("Departamento agregado exitosamente")
    
    def mostrarTodos(self):
        print("\n--- Lista de Departamentos ---")
        departamentos = ReglasDepartamento.mostrarTodos()
        if departamentos:
            for dept in departamentos:
                print(dept)
        else:
            print("No hay departamentos registrados")
    
    def buscarPorCodigo(self):
        print("\n--- Buscar Departamento por ID ---")
        id_dept = int(input("ID del departamento: "))
        departamento = ReglasDepartamento.buscarPorCodigo(id_dept)
        if departamento:
            print(departamento)
        else:
            print("Departamento no encontrado")
    
    def buscarPorNombre(self):
        print("\n--- Buscar Departamento por Nombre ---")
        nombre = input("Nombre del departamento: ")
        departamentos = ReglasDepartamento.buscarPorNombre(nombre)
        if departamentos:
            for dept in departamentos:
                print(dept)
        else:
            print("No se encontraron departamentos")
    
    def modificar(self):
        print("\n--- Modificar Departamento ---")
        id_dept = int(input("ID del departamento a modificar: "))
        departamento = ReglasDepartamento.buscarPorCodigo(id_dept)
        if departamento:
            print(f"Departamento actual: {departamento}")
            nuevo_nombre = input("Nuevo nombre: ")
            departamento.nombre = nuevo_nombre
            
            if ReglasDepartamento.modificar(departamento):
                print("Departamento modificado exitosamente")
        else:
            print("Departamento no encontrado")
    
    def eliminar(self):
        print("\n--- Eliminar Departamento ---")
        id_dept = int(input("ID del departamento a eliminar: "))
        departamento = ReglasDepartamento.buscarPorCodigo(id_dept)
        if departamento:
            print(f"Departamento a eliminar: {departamento}")
            confirmacion = input("¿Está seguro? (s/n): ")
            if confirmacion.lower() == 's':
                if ReglasDepartamento.eliminar(id_dept):
                    print("Departamento eliminado exitosamente")
        else:
            print("Departamento no encontrado")