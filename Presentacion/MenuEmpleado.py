from Presentacion.MenuBase import MenuBase
from Dominio.DTO.Empleado import Empleado
from Aplicacion import ReglasEmpleado
from datetime import datetime

class MenuEmpleado(MenuBase):
    def __init__(self):
        super().__init__("Gestión de Empleados")
    
    def agregar(self):
        print("\n--- Agregar Empleado ---")
        run = input("RUN: ")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        direccion = input("Dirección: ")
        fono = input("Teléfono: ")
        correo = input("Correo: ")
        fecha_contrato = input("Fecha contrato (YYYY-MM-DD): ")
        id_departamento = int(input("ID Departamento: "))
        
        empleado = Empleado(run=run, nombre=nombre, apellidos=apellidos, 
                          direccion=direccion, fono=fono, correo=correo,
                          fecha_contrato=fecha_contrato, id_departamento=id_departamento)
        
        if ReglasEmpleado.agregar(empleado):
            print("Empleado agregado exitosamente")
    
    def mostrarTodos(self):
        print("\n--- Lista de Empleados ---")
        empleados = ReglasEmpleado.mostrarTodos()
        if empleados:
            for emp in empleados:
                print(emp)
        else:
            print("No hay empleados registrados")
    
    def buscarPorCodigo(self):
        print("\n--- Buscar Empleado por ID ---")
        id_emp = int(input("ID del empleado: "))
        empleado = ReglasEmpleado.buscarPorCodigo(id_emp)
        if empleado:
            print(empleado)
        else:
            print("Empleado no encontrado")
    
    def buscarPorNombre(self):
        print("\n--- Buscar Empleado por Nombre ---")
        nombre = input("Nombre del empleado: ")
        empleados = ReglasEmpleado.buscarPorNombre(nombre)
        if empleados:
            for emp in empleados:
                print(emp)
        else:
            print("No se encontraron empleados")
    
    def modificar(self):
        print("\n--- Modificar Empleado ---")
        id_emp = int(input("ID del empleado a modificar: "))
        empleado = ReglasEmpleado.buscarPorCodigo(id_emp)
        if empleado:
            print(f"Empleado actual: {empleado}")
            empleado.run = input(f"RUN ({empleado.run}): ") or empleado.run
            empleado.nombre = input(f"Nombre ({empleado.nombre}): ") or empleado.nombre
            empleado.apellidos = input(f"Apellidos ({empleado.apellidos}): ") or empleado.apellidos
            empleado.direccion = input(f"Dirección ({empleado.direccion}): ") or empleado.direccion
            empleado.fono = input(f"Teléfono ({empleado.fono}): ") or empleado.fono
            empleado.correo = input(f"Correo ({empleado.correo}): ") or empleado.correo
            empleado.fecha_contrato = input(f"Fecha contrato ({empleado.fecha_contrato}): ") or empleado.fecha_contrato
            empleado.id_departamento = int(input(f"ID Departamento ({empleado.id_departamento}): ") or empleado.id_departamento)
            
            if ReglasEmpleado.modificar(empleado):
                print("Empleado modificado exitosamente")
        else:
            print("Empleado no encontrado")
    
    def eliminar(self):
        print("\n--- Eliminar Empleado ---")
        id_emp = int(input("ID del empleado a eliminar: "))
        empleado = ReglasEmpleado.buscarPorCodigo(id_emp)
        if empleado:
            print(f"Empleado a eliminar: {empleado}")
            confirmacion = input("¿Está seguro? (s/n): ")
            if confirmacion.lower() == 's':
                if ReglasEmpleado.eliminar(id_emp):
                    print("Empleado eliminado exitosamente")
        else:
            print("Empleado no encontrado")