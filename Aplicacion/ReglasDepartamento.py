from Persistencia.DAO import DepartamentoDAO

def agregar(departamento):
    if not departamento.nombre.strip():
        raise ValueError("El nombre del departamento no puede estar vacío")
    return DepartamentoDAO.agregar(departamento)

def modificar(departamento):
    if not departamento.nombre.strip():
        raise ValueError("El nombre del departamento no puede estar vacío")
    return DepartamentoDAO.modificar(departamento)

def eliminar(id_departamento):
    if id_departamento <= 0:
        raise ValueError("ID de departamento inválido")
    return DepartamentoDAO.eliminar(id_departamento)

def mostrarTodos():
    return DepartamentoDAO.mostrarTodos()

def buscarPorCodigo(id_departamento):
    if id_departamento <= 0:
        raise ValueError("ID de departamento inválido")
    return DepartamentoDAO.buscarPorCodigo(id_departamento)

def buscarPorNombre(nombre):
    if not nombre.strip():
        raise ValueError("El nombre a buscar no puede estar vacío")
    return DepartamentoDAO.buscarPorNombre(nombre)