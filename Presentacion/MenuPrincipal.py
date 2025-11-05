from Presentacion.MenuDepartamento import MenuDepartamento
from Presentacion.MenuEmpleado import MenuEmpleado
from Presentacion.MenuProyecto import MenuProyecto

class MenuPrincipal:
    def __init__(self):
        self.menu_departamento = MenuDepartamento()
        self.menu_empleado = MenuEmpleado()
        self.menu_proyecto = MenuProyecto()
    
    def mostrar_menu(self):
        print("\n=== SISTEMA DE GESTIÓN DE PERSONAL ===")
        print("1. Gestión de Departamentos")
        print("2. Gestión de Proyectos")
        print("3. Gestión de Empleados")
        print("4. Salir")
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    self.menu_departamento.ejecutar()
                elif opcion == 2:
                    self.menu_proyecto.ejecutar()
                elif opcion == 3:
                    self.menu_empleado.ejecutar()
                elif opcion == 4:
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción inválida")
            except ValueError:
                print("Por favor ingrese un número válido")
            except Exception as e:
                print(f"Error: {str(e)}")