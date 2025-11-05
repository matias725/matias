from abc import ABC, abstractmethod

class MenuBase(ABC):
    def __init__(self, titulo):
        self.titulo = titulo
    
    def mostrar_menu(self):
        print(f"\n=== {self.titulo} ===")
        print("1. Agregar")
        print("2. Mostrar Todos")
        print("3. Buscar por ID")
        print("4. Buscar por Nombre")
        print("5. Modificar")
        print("6. Eliminar")
        print("7. Volver al Menú Principal")
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    self.agregar()
                elif opcion == 2:
                    self.mostrarTodos()
                elif opcion == 3:
                    self.buscarPorCodigo()
                elif opcion == 4:
                    self.buscarPorNombre()
                elif opcion == 5:
                    self.modificar()
                elif opcion == 6:
                    self.eliminar()
                elif opcion == 7:
                    break
                else:
                    print("Opción inválida")
            except ValueError:
                print("Por favor ingrese un número válido")
            except Exception as e:
                print(f"Error: {str(e)}")
    
    @abstractmethod
    def agregar(self):
        pass
    
    @abstractmethod
    def mostrarTodos(self):
        pass
    
    @abstractmethod
    def buscarPorCodigo(self):
        pass
    
    @abstractmethod
    def buscarPorNombre(self):
        pass
    
    @abstractmethod
    def modificar(self):
        pass
    
    @abstractmethod
    def eliminar(self):
        pass